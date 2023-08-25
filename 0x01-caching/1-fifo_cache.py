#!/usr/bin/env python3
"""
subclass Caching system that uses the FIFO algorithm -> first in first out
"""

BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFO class that has different methods for handling the caching
    system
    """

    def __init__(self):
        """
        initialize a sub class of BaseCaching system with class variable
        order for storing the order of the caching system
        this system uses the FIFO ->first in first out algorithm
        """
        super(FIFOCache, self).__init__()
        self.order = []

    def put(self, key, item):
        """
        put method that add items to the dictionary of the sub class
        caching system
        """
        try:
            assert key is not None and item is not None
        except AssertionError:
            return None
        length = len(self.cache_data)
        if (length >= self.MAX_ITEMS) and key not in self.cache_data:
            print(f"DISCARD: {self.order[0]}")
            del self.cache_data[self.order[0]]
            del self.order[0]
        if key not in self.order:
            self.order.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """
        get method that remove item from the dictionary in a FIFO
        algorithm style for the subclass caching system
        """
        try:
            assert key in self.cache_data().keys() and key is not None
        except AssertionError:
            return None
        return self.cache_data.get(key)
