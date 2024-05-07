from base_caching import BaseCaching

class FIFOCache(BaseCaching):
    """ FIFOCache class inherits from BaseCaching and implements a FIFO caching system """

    def __init__(self):
        """ Initialize the FIFOCache """
        super().__init__()
        self.keys_queue = []

    def put(self, key, item):
        """ Add an item to the cache """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                oldest_key = self.keys_queue[0]
                del self.cache_data[oldest_key]
                print("DISCARD: {}".format(oldest_key))
                self.keys_queue.pop(0)

            self.cache_data[key] = item
            self.keys_queue.append(key)

    def get(self, key):
        """ Retrieve an item from the cache """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
    