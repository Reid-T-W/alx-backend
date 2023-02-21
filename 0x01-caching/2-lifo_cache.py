#!/usr/bin/env python3
"""
Caching class that inherits from the base class, BaseCashing
Has limited cashing capabilities
Implements the LIFO caching algorithim
"""
from collections import deque
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    Caching class that inherits from the base class, BaseCashing
    Has limited cashing capabilities
    Implements the LIFO caching algorithim
    """
    def __init__(self) -> None:
        """
        Creates the dictionary and list object
        """
        super().__init__()
        self.stack = deque([], 4)

    def put(self, key, item):
        """
        Method that populates the cache given a key and item
        The LIFO caching algorithim is used to populate the
        cache
        """
        if key is None or item is None:
            return

        # Checking if the key exists in the
        # dictionary, and performing a simple
        # insert
        if key in self.cache_data.keys():
            # The key is moved to the end of the
            # stack, since it was updated last
            self.stack.remove(key)
            self.stack.append(key)
            self.cache_data[key] = item
        else:
            # Checking if the cache limit has reached
            # and removing the last key that was inserted
            if (len(self.stack) == BaseCaching.MAX_ITEMS):
                removed_key = self.stack.pop()
                self.cache_data.pop(removed_key)
                print("DISCARD: {}".format(removed_key))
            self.stack.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        Method that retrieves the data from the cache given
        the key
        """
        return(self.cache_data.get(key, None))
