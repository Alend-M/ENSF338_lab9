class DLeftHashTable:
    def __init__(self, entries, buckets):
        self.left_table = [[] for _ in range(entries)]
        self.right_table = [[] for _ in range(entries)]
        self.entries = entries
        self.buckets = buckets

    def insert(self, key, value):
        left_hash = hash(key) % self.entries
        right_hash = hash(key[::-1]) % self.entries

        if len(self.left_table[left_hash]) <= len(self.right_table[right_hash]):
            self.left_table[left_hash].append((key, value))
        else:
            self.right_table[right_hash].append((key, value))

    def lookup(self, key):
        left_hash = hash(key) % self.entries
        right_hash = hash(key[::-1]) % self.entries

        for k, v in self.left_table[left_hash]:
            if k == key:
                return v

        for k, v in self.right_table[right_hash]:
            if k == key:
                return v

        return None

# Example usage:
dleft_table = DLeftHashTable(entries=10, buckets=5)
dleft_table.insert("apple", 5)
dleft_table.insert("banana", 10)
dleft_table.insert("orange", 15)

print(dleft_table.lookup("apple"))  # Output: 5
print(dleft_table.lookup("banana")) # Output: 10
print(dleft_table.lookup("grape"))  # Output: None
