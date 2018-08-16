import time
class LRUCache(object):
    capacity = 0
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.dict = {}
        self.use = {}

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.dict:
            return -1
        else:
            self.use[key] = time.time()
            return self.dict[key]

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.dict:
            self.use[key] = time.time()
            self.dict[key] = value
        else:
            if len(self.dict) >= self.capacity:
                minvalue = float("inf")
                tkey = 0
                for i in self.use.keys():
                    if self.use[i] < minvalue:
                        minvalue = self.use[i]
                        tkey = i
                self.dict.pop(tkey)
                self.use.pop(tkey)
                self.dict[key] = value
                self.use[key] = time.time()

            else:
                self.dict[key] = value
                self.use[key] = time.time()

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
t = LRUCache(2)
t.put(2, 1)
t.put(2, 2)
print t.get(2)
t.put(1, 1)
t.put(4, 1)
print t.get(2)