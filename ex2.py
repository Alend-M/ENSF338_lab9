import random
import string
import matplotlib.pyplot as plt

class DLeftHashTable:
    def __init__(self, entries, buckets):
        self.left_table = [[] for _ in range(entries)]
        self.right_table = [[] for _ in range(entries)]
        self.entries = entries
        self.buckets = buckets

    def _hash(self, key):
        hash_value = 0
        for char in key:
            hash_value += ord(char)
        return hash_value % self.entries

    def insert(self, key, value):
        left_hash = self._hash(key) % self.entries
        right_hash = self._hash(key[::-1]) % self.entries

        if len(self.left_table[left_hash]) <= len(self.right_table[right_hash]):
            self.left_table[left_hash].append((key, value))
        else:
            self.right_table[right_hash].append((key, value))

    def lookup(self, key):
        left_hash = self._hash(key) % self.entries
        right_hash = self._hash(key[::-1]) % self.entries

        for k, v in self.left_table[left_hash]:
            if k == key:
                return v

        for k, v in self.right_table[right_hash]:
            if k == key:
                return v

        return None

def generate_random_string(length):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def simulate_hash_table(entries, num_strings):
    dleft_table = DLeftHashTable(entries=entries, buckets=5)
    collisions_left = [0] * entries
    collisions_right = [0] * entries

    for _ in range(num_strings):
        key = generate_random_string(random.randint(1, 10))
        dleft_table.insert(key, None)

    for i in range(entries):
        collisions_left[i] = len(dleft_table.left_table[i])
        collisions_right[i] = len(dleft_table.right_table[i])

    return collisions_left, collisions_right

num_strings = 1000000
entries = 1000

collisions_left, collisions_right = simulate_hash_table(entries, num_strings)

index_values = list(range(entries))

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.bar(index_values, collisions_left, label='Left Hash Collisions')
plt.xlabel('Index Value')
plt.ylabel('Number of Collisions')
plt.title('Left Hash Collision Distribution')
plt.legend()

plt.subplot(1, 2, 2)
plt.bar(index_values, collisions_right, label='Right Hash Collisions', color = 'orange')
plt.xlabel('Index Value')
plt.ylabel('Number of Collisions')
plt.title('Right Hash Collision Distribution')
plt.legend()

plt.tight_layout()
plt.show()

# In this context, 'hot spots' are the locations where the number of 
# collisions are noticably higher than the rest of the distrubtion. In
# other words, the locations where there are 'spikes' in the graph.
# Both graphs show one major hot spot around index value 100, and another
# right before index value 200.