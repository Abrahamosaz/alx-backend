#!/usr/bin/env python3
"""
subclass system that implement the LIFO algorithm -> last in first out
"""

BaseCaching = __import__("base_caching").BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFO class that has different methods for handling the caching
    system
    """

    def __init__(self):
        """
        initialize a sub class of BaseCaching system with class variable
        order for storing the order of the caching system
        this system uses the LIFO->last in first out algorithm
        """
        super(LIFOCache, self).__init__()
        self.order = []

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
        if (length >= self.MAX_ITEMS) and key not in self.cache_data:
            print(f"DISCARD: {self.order[-1]}")
            del self.cache_data[self.order[-1]]
            del self.order[-1]
        if key not in self.order:
            self.order.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """
        get method that remove item from the dictionary in a LIFO
        algorithm style for the subclass caching system
        """
        try:
            assert key is not None and key in self.cache_data
        except AssertionError:
            return None
        return self.cache_data[key]
