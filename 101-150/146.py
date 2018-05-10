import queue
class LRUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.queue = queue.Queue()
        self.value = {}
        self.num = {}

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if self.num[key] > 0:
            self.queue.put(key)
            return self.value[key]
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        self.queue.put(key)
        self.value[key] = value
        if key in self.num:
            self.num[key] += 1
        else:
            self.num[key] = 1
        self.capacity -= 1
        if self.capacity == -1:
            self.capacity = 0
            x = self.queue.get()
            self.num[x] -= 1
            while self.num[x]:
                x = self.queue.get()
                self.num[x] -= 1