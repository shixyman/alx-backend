from base_caching import BaseCaching

class LIFOCache(BaseCaching):
    """ LIFOCache class inherits from BaseCaching and implements a LIFO caching system """

    def __init__(self):
        """ Initialize the LIFOCache """
        super().__init__()
        self.keys_stack = []

    def put(self, key, item):
        """ Add an item to the cache """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                last_key = self.keys_stack.pop()
                del self.cache_data[last_key]
                print("DISCARD: {}".format(last_key))

            self.cache_data[key] = item
            self.keys_stack.append(key)

    def get(self, key):
        """ Retrieve an item from the cache """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
