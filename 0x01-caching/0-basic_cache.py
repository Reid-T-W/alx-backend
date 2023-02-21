#!/usr/bin/env python3
"""
Caching class that inherits from the base class, BaseCashing
Has unlimited cashing capabilities
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    Caching class that inherits from the base class, BaseCashing
    Has unlimited cashing capabilities
    """
    def put(self, key, item):
        """
        Method that populates the cache given a key and item
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """
        Method that retrieves the data from the cache given
        the key
        """
        return(self.cache_data.get(key, None))
