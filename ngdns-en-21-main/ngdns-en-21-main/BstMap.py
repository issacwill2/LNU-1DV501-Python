from dataclasses import dataclass
from typing import Any

# The BstMap class is a binary search tree based implementation of
# a map (or dictionary). It works for any type of values and for
# all types keys that are comparable ==> we can compare keys using
# the operators < and >.

#
# The Node class is responsible for most of the work.
# Each call to the BstMap class is just delegated to the
# root node which starts a recursive sequence of calls to
# handle the request. Notice: All Node methods are recursive.
@dataclass
class Node:
    key: Any = None         # the key
    value: Any = None       # the value
    left: Any = None        # left child (a Node)
    right: Any = None       # right child (a Node)

    def put(self, key, value):
        if key < self.key:
            # add it to leftsubtree
            if self.left is None:
                self.left = Node(key, value)
            else:
                self.left.put(key, value)
        elif key == self.key:
            self.value = value
        if key > self.key:
            # add to right subtree
            if self.right is None:
                self.right = Node(key, value)
            else:
                self.right.put(key, value)

    def to_string(self):
        tree_1 = ''
        if self.left is not None:
            tree_1 += self.left.to_string()
        tree_1 += f'({self.key},{self.value}) '
        if self.right is not None:
            tree_1 += self.right.to_string()
        return tree_1

    def count(self):
        s_count = 1
        if self.left is not None:
            s_count += self.left.count()
        if self.right is not None:
            s_count += self.right.count()
        return s_count

    def get(self, key):
        value = None
        if self.key == key:
            return self.value
        if self.left is not None:
            if self.key >= key:
                value = self.left.get(key)
            if value is not None:
                return value
        if self.right is not None:
            if self.key <= key:
                value = self.right.get(key)
            if value is not None:
                return value
        return value

    def max_depth(self):
        if self.key is None:
            return 0
        else:
            left_dep = 0
            right_dep = 0
            if self.left:
                left_dep = self.left.max_depth()
            if self.right:
                right_dep = self.right.max_depth()
            if (left_dep > right_dep):
                return left_dep + 1
            else:
                return right_dep + 1

    def as_list(self, lst):
        if self.left is not None:
            self.left.as_list(lst)
        lst.append((self.key, self.value))
        if self.right is not None:
            self.right.as_list(lst)
        return lst

    def to_list(self):
        lst = []
        if self.left:
            lst += self.left.to_list()
        # print([tuple([self.key,self.value])])
        # print(type([tuple([self.key,self.value])]))
        if self.key:
            lst.append(tuple([self.key, self.value]))
        if self.right:
            lst += self.right.to_list()
        return lst

# The BstMap class is rather simple. It basically just takes care
# of the case when the map is empty. All other cases are delegated
# to the root node ==> the Node class.
#
# The class below is complete ==> not to be changed


@dataclass
class BstMap:
    root: Node = None

    # Adds a key-value pair to the map
    def put(self, key, value):
        if self.root is None:    # Empty, add first node
            self.root = Node(key, value, None, None)
        else:
            self.root.put(key, value)

    # Returns a string representation of all the key-value pairs
    def to_string(self):
        if self.root is None:     # Empty, return empty brackets
            return "{ }"
        else:
            res = "{ "
            res += self.root.to_string()
            res += "}"
            return res

    # Returns the current number of key-value pairs in the map
    def size(self):
        if self.root is None:
            return 0
        else:
            return self.root.count()

    # Returns the value for a given key. Returns None
    # if key doesn't exist (or map is empty)
    def get(self, key):
        if self.root is None:
            return None
        else:
            return self.root.get(key)

    # Returns the maximum tree depth. That is, the length
    # (counted in nodes) of the longest root-to-leaf path
    def max_depth(self):
        if self.root is None:
            return 0
        else:
            return self.root.max_depth()

    # Returns a sorted list of all key-value pairs in the map.
    # Each key-value pair is represented as a tuple and the
    # list is sorted on the keys ==> left-to-right in-order
    def as_list(self):
        lst = []
        if self.root is None:
            return lst
        else:
            return self.root.as_list(lst)
