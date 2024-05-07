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
            if len(self.cache_data) >= self.MAX_ITEMS:
                if self.MAX_ITEMS <= 0:
                    return

                least_frequent_keys = []
                min_frequency = min(self.frequency.values())

                for k, v in self.cache_data.items():
                    if self.frequency[k] == min_frequency:
                        least_frequent_keys.append(k)

                least_recently_used_key = None
                if len(least_frequent_keys) > 1:
                    for k in self.frequency.keys():
                        if k in least_frequent_keys:
                            if least_recently_used_key is None:
                                least_recently_used_key = k
                            elif self.frequency[k] < self.frequency[least_recently_used_key]:
                                least_recently_used_key = k

                if least_recently_used_key is None:
                    least_recently_used_key = least_frequent_keys[0]

                del self.cache_data[least_recently_used_key]
                del self.frequency[least_recently_used_key]
                print("DISCARD: {}".format(least_recently_used_key))

            self.cache_data[key] = item
            self.frequency[key] = 1
            self.min_frequency = 1

    def get(self, key):
        """ Retrieve an item from the cache """
        if key is not None and key in self.cache_data:
            self.frequency[key] += 1
            return self.cache_data[key]
        return None