from base_caching import BaseCaching

class BasicCache(BaseCaching):
    """ BasicCache class inherits from BaseCaching and implements a basic caching system """

    def put(self, key, item):
        """ Add an item to the cache """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Retrieve an item from the cache """
        if key is not None:
            return self.cache_data.get(key)
        return None