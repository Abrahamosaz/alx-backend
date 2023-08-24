#!/usr/bin/env python3
"""
caching class for different caching types
"""

BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):

    """
    Basic caching class system using python dictionary for caching data
    """

    def put(self, key, item):
        """
        put methods that add items to the dictionary
        of the caching system
        """
        try:
            assert key is not None and item is not None
        except AssertionError:
            return
        self.cache_data[key] = item

    def get(self, key):
        """
        get method that retrieve items from the dictionary
        caching system class
        """
        try:
            assert key in self.cache_data.keys() and key is not None
        except AssertionError:
            return None
        return self.cache_data.get(key)
