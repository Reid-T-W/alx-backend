#!/usr/bin/env python3
"""
Caching class that inherits from the base class, BaseCashing
Has limited cashing capabilities
Implements the FIFO caching algorithim
"""
from collections import deque
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    Caching class that inherits from the base class, BaseCashing
    Has limited cashing capabilities
    Implements the FIFO caching algorithim
    """
    def __init__(self) -> None:
        """
        Creates the dictionary and deque object
        """
        super().__init__()
        self.queue = deque([], 4)

    def put(self, key, item):
        """
        Method that populates the cache given a key and item
        The FIFO caching algorithim is used to populate the
        cache
        """
        if key is None or item is None:
            return

        # Checking if the key exists in the
        # dictionary, and performing a simple
        # insert
        if key in self.cache_data.keys():
            self.cache_data[key] = item
        else:
            # Checking if the cache limit has reached
            # and removing the first key that was inserted
            if (len(self.queue) == 4):
                removed_key = self.queue.popleft()
                self.cache_data.pop(removed_key)
                print("DISCARD: {}".format(removed_key))
            self.queue.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        Method that retrieves the data from the cache given
        the key
        """
        return(self.cache_data.get(key, None))
