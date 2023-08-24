#!/usr/bin/env python3
"""
subclass Caching system that uses the
LRU algorithm -> least recent use algorithm
"""

BaseCaching = __import__("base_caching").BaseCaching


class LRUCache(BaseCaching):
    """
    LRU class that has different methods for handling the caching
    system
    """

    def __init__(self):
        """
        initialize a sub class of BaseCaching system with class variable
        usage for storing the order of the caching system
        this system uses the LRU->least recent use algorithm
        """
        super(LRUCache, self).__init__()
        self.usage = []

    def put(self, key, item):
        """
        put method that add items to the dictionary of the sub class
        caching system
        """
        try:
            assert key is not None and item is not None
        except AssertionError:
            return

        length = len(self.cache_data)
        if (length >= self.MAX_ITEMS and key not in self.cache_data):
            print(f"DISCARD: {self.usage[0]}")
            del self.cache_data[self.usage[0]]
            del self.usage[0]
        if key in self.usage:
            del self.usage[self.usage.index(key)]
        self.usage.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """
        get method that remove item from the dictionary in a
        LRU algorithm style for the subclass caching system
        """
        try:
            assert key is not None and key in self.cache_data
        except AssertionError:
            return None

        if key in self.usage:
            del self.usage[self.usage.index(key)]
            self.usage.append(key)
        return self.cache_data[key]
