from dataclasses import dataclass
from typing import List


@dataclass
class HashSet:
    buckets: List[List] = None
    size: int = 0

    def init(self):
        self.size = 0
        self.buckets = [[] for i in range(8)]

    # Computes hash value for a word (a string)
    def get_hash(self, word):
        hash_1 = 0
        num = 1
        for char in word.lower():
            hash_1 += num * ord(char)
            num += 1
        return hash_1 % len(self.buckets)

    # Doubles size of bucket list
    def rehash(self):
        bucket_new = []
        for i in self.buckets:
            for value in i:
                bucket_new.append(value)
        new_buckets = [[] for i in range(len(self.buckets))]
        self.buckets.extend(new_buckets)
        for lst in self.buckets:
            lst.clear()
        self.size = 0
        for i in bucket_new:
            self.add(i)

    # Adds a word to set if not already added
    def add(self, word):
        hash_2 = self.get_hash(word)
        bucket = self.buckets[hash_2]
        if word not in bucket:
            bucket.append(word)
            self.size += 1
            if self.size == len(self.buckets):
                self.rehash()

    def to_string(self):
        string_1 = "{ "
        for i in self.buckets:
            for j in i:
                string_1 += j + " "
        string_1 += "}"
        return string_1

    # Returns current number of elements in set
    def get_size(self):
        return self.size

    # Returns True if word in set, otherwise False
    def contains(self, word):
        for i in self.buckets:
            if word in i:
                return True
        return False

    # Returns current size of bucket list
    def bucket_list_size(self):
        return len(self.buckets)

    # Removes word from set if there, does nothing
    # if word not in set
    def remove(self, word):
        for i in self.buckets:
            if word in i:
                i.remove(word)
                self.size -= 1

    # Returns the size of the bucket with most elements
    def max_bucket_size(self):
        size_max = 0
        for i in self.buckets:
            size = len(i)
            if size_max < size:
                size_max = size
        return size_max
