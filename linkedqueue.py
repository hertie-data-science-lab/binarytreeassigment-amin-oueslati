# -*- coding: utf-8 -*-
"""
Submitted on 2nd April 2023

@authors: Oskar Krafft | Paul Sharratt | Fabian Metz | Amin Oueslati
"""

class LinkedQueue:
    """FIFO queue implementation using a singly linked list for storage."""

    def __init__(self):
        self._first = None  
        self._last = None  
        self._length = 0 

    def is_empty(self):
        return self._first is None

    def enqueue(self, item):
        oldLast = self._last
        self._last = _Node(item, None)
        if self.is_empty():
            self._first = self._last
        else:
            oldLast.next = self._last
        self._length += 1

    def dequeue(self):
        item = self._first.item
        self._first = self._first.next
        if self.is_empty():
            self._last = None
        self._length -= 1
        return item

    def __len__(self):
        return self._length

class _Node:
    def __init__(self, item, next):
        self.item = item  # Reference to an item
        self.next = next  # Reference to the next _Node object