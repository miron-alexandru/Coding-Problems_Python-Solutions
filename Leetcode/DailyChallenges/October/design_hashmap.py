# problem link: https://leetcode.com/problems/design-hashmap/

# my solution:

class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.buckets = [None] * self.size

    def _hash(self, key):
        return key % self.size

    def put(self, key: int, value: int) -> None:
        hash_key = self._hash(key)
        if not self.buckets[hash_key]:
            self.buckets[hash_key] = []
        for i, (k, v) in enumerate(self.buckets[hash_key]):
            if k == key:
                self.buckets[hash_key][i] = (key, value)
                return
        self.buckets[hash_key].append((key, value))

    def get(self, key: int) -> int:
        hash_key = self._hash(key)
        if not self.buckets[hash_key]:
            return -1
        for k, v in self.buckets[hash_key]:
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        hash_key = self._hash(key)
        if not self.buckets[hash_key]:
            return
        for i, (k, v) in enumerate(self.buckets[hash_key]):
            if k == key:
                del self.buckets[hash_key][i]
                return
