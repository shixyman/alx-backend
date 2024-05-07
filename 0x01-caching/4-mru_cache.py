from base_caching import BaseCaching

class MRUCache(BaseCaching):
    """ MRUCache class inherits from BaseCaching and implements an MRU caching system """

    def __init__(self):
        """ Initialize the MRUCache """
        super().__init__()
        self.keys_queue = []

    def put(self, key, item):
        """ Add an item to the cache """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                most_recent_key = self.keys_queue.pop()
                del self.cache_data[most_recent_key]
                print("DISCARD: {}".format(most_recent_key))

            self.cache_data[key] = item
            if key in self.keys_queue:
                self.keys_queue.remove(key)
            self.keys_queue.append(key)

    def get(self, key):
        """ Retrieve an item from the cache """
        if key is not None and key in self.cache_data:
            self.keys_queue.remove(key)
            self.keys_queue.append(key)
            return self.cache_data[key]
        return None
