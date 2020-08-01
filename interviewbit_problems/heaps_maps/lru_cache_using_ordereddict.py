from collections import OrderedDict


class LRUCache():
    def __init__(self, capacity):
        """
        capacity of the cache
        queue is ordereded dictonary, so ordering of items are preserved.
        """
        self.capacity = capacity
        self.hash_map = OrderedDict()

    def get_key(self, key):
        """get the key from dict. If the key is available move it to end"""
        if key in self.hash_map:
            self.hash_map.move_to_end(key)
        return self.hash_map.get(key, -1)

    def set_value(self, key, value):
        """put the key to the dict if the length is lessthan capicty else remove the first item from the queue and insert to queue.
                """
        if len(self.hash_map) < self.capacity:
            if key in self.hash_map:
                self.hash_map[key] = value
                self.hash_map.move_to_end(key)
            else:
                self.hash_map[key] = value
        else:
            if key in self.hash_map:
                self.hash_map[key] = value
                self.hash_map.move_to_end(key)
            else:
                self.hash_map.popitem(last=False)
                self.hash_map[key] = value
