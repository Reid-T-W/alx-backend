#!/usr/bin/env python3
"""
Caching class that inherits from the base class, BaseCashing
Has limited cashing capabilities
Implements the LFU caching algorithim, if more than one is
found, the LRU algorithim will be used.
"""
import sys
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """
    Caching class that inherits from the base class, BaseCashing
    Has limited cashing capabilities (limited space)
    Implements the LFU caching algorithim, if more than one is
    found, the LRU algorithim will be used.
    """
    def __init__(self) -> None:
        """
        Creates the dictionary and list object
        """
        super().__init__()
        self.access_dict = {}
        self.age_dict = {}
        self.counter = 0

    def put(self, key, item):
        """
        Method that populates the cache given a key and item
        The LFU caching algorithim is used to populate the
        cache, if more than one is found, the LRU algorithim
        will be used.
        """
        if key is None or item is None:
            return
        # Checking if the key exists in the
        # dictionary, and performing an insert
        # into the actual dictionary and age
        # tracking dictionary
        if key in self.cache_data.keys():
            self.cache_data[key] = item
            self.age_dict[key] = self.counter
            self.counter += 1
            # For LFU algorithim
            self.access_dict[key] += 1
        else:
            # Checking if the cache limit has reached
            if (len(self.cache_data) == BaseCaching.MAX_ITEMS):
                # For LFU algorithim
                min_freq_value = sys.maxsize
                min_freq_key = None
                for k, freq in self.access_dict.items():
                    if freq < min_freq_value:
                        min_freq_value = freq
                        min_freq_key = k

                if ([self.access_dict.values()].count(min_freq_value) == 1):
                    self.cache_data.pop(min_freq_key)
                    print("DISCARD: {}".format(min_freq_key))
                    self.access_dict.pop(min_freq_key)
                    self.age_dict.pop(min_freq_key)
                else:
                    subset_age_dict = {}
                    # Find all keys that have similar frequencies
                    # and populating subset of the age dict specifically
                    # for those keys
                    for ke, val in self.access_dict.items():
                        if val == min_freq_value:
                            subset_age_dict[ke] = self.age_dict[ke]

                    # Get the key (k) with the smallest age
                    # from the subset_age_dict
                    min_age_value = sys.maxsize
                    min_age_key = None
                    for k, age in subset_age_dict.items():
                        if age < min_age_value:
                            min_age_value = age
                            min_age_key = k

                    # Remove the key with minimum age from the
                    # actual dictionary and age_dictinary
                    self.cache_data.pop(min_age_key)
                    print("DISCARD: {}".format(min_age_key))
                    self.age_dict.pop(min_age_key)
                    self.access_dict.pop(min_freq_key)

            # Inserting the new key and item, while also
            # assigning it an age
            self.cache_data[key] = item

            # Handling LRU caching
            self.age_dict[key] = self.counter
            self.counter += 1

            # Handling LFU caching
            self.access_dict[key] = 1

    def get(self, key):
        """
        Method that retrieves the data from the cache given
        the key
        """
        value = self.cache_data.get(key, None)

        # Handling LRU
        if value is not None:
            # Updating the age of the key
            self.age_dict[key] = self.counter
            self.counter += 1

            # Handling LFU
            self.access_dict[key] += 1
        return value
