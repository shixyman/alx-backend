from base_caching import BaseCaching

class LFUCache(BaseCaching):
    """ LFUCache class inherits from BaseCaching and implements an LFU caching system """

    def __init__(self):
        """ Initialize the LFUCache """
        super().__init__()
        self.frequency = {}
        self.min_frequency = 0

    def put(self, key, item):
        """ Add an item to the cache """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data[key] = item
                self.frequency[key] += 1
            else:
                if len(self.cache_data) >= self.MAX_ITEMS:
                    while self.cache_data and self.frequency[min(self.cache_data, key=self.frequency.get)] > self.min_frequency:
                        least_frequent_keys = [k for k, v in self.frequency.items() if v == self.min_frequency]
                        lru_key = min(self.cache_data, key=lambda k: self.cache_data[k])
                        if lru_key in least_frequent_keys:
                            break
                        del self.cache_data[lru_key]
                        del self.frequency[lru_key]
                        print("DISCARD: {}".format(lru_key))

                self.cache_data[key] = item
                self.frequency[key] = 1
                self.min_frequency = 1

    def get(self, key):
        """ Retrieve an item from the cache """
        if key is not None and key in self.cache_data:
            self.frequency[key] += 1
            return self.cache_data[key]
        return None
