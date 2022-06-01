from dataclasses import dataclass
from typing import Any

# A head-and-tail implementation of a deque using data classes


# Each node is an instance of class Node
@dataclass
class Node:
    value: int = None
    nxt: Any = None  # Any since Node not properly defined at this point


@dataclass
class Deque:
    head: Node = None      # First node in queue
    tail: Node = None      # Last node in queue
    size: int = 0
    # Add value n as first entry in deque

    def add_first(self, n):
        node_new = Node(n)
        node_new.nxt = self.head
        self.head = node_new
        self.size += 1
        if self.tail is None:
            self.tail = self.head
    # Returns a string representation of the current deque content

    def to_string(self):
        outcome = "{ "
        available = self.head
        for _ in range(self.size):
            outcome += str(available.value)
            available = available.nxt
            if available is not None:
                outcome += ", "
        return outcome + " }"
    # Add value n as last entry in deque

    def add_last(self, n):
        node_new = Node(n)
        if self.tail is None:
            self.head = self.tail = node_new
        else:
            self.tail.nxt = node_new
            self.tail = self.tail.nxt
        self.size += 1
    # Returns (without removing) the last entry in the deque.
    # Gives error message and returns None when accessing empty deque.

    def get_last(self):
        if self.size == 0:
            print("You can't access an empty queue")
            return None
        else:
            return self.tail.value
    # Returns (without removing) the first entry in the deque
    # Gives error message and returns None when accessing empty deque.

    def get_first(self):
        if self.size == 0:
            print("You can't access an empty queue")
            return None
        else:
            return self.head.value
    # Removes and returns the first entry in the deque.
    # Gives error message and returns None when accessing empty deque.
    # The case size = 1 requires speciall handling

    def remove_first(self):
        if self.size == 0:
            print("You can't access an empty queue")
            return None
        else:
            for_now = self.head
            self.head = self.head.nxt
            self.size -= 1
            if self.head is None:
                self.tail = None
            return for_now.value
    # Removes and returns the last entry in the deque.
    # Gives error message and returns None when accessing empty deque.
    # The case size = 1 requires speciall handling

    def remove_last(self):
        if self.size == 0:
            print("You can't access an empty queue")
            return None
        elif self.size == 1:
            for_now = self.head
            self.head = self.tail = None
            self.size = 0
            return for_now.value
        else:
            current = self.head
            for i in range(self.size - 2):
                current = current.nxt
            temp = self.tail
            self.tail = current
            self.tail.nxt = None
            self.size -= 1
            return temp.value
