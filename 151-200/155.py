import queue
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        if self.min == []:
            self.min.append(x)
        else:
            if x <= self.min[-1]:
                self.min.append(x)

    def pop(self):
        """
        :rtype: void
        """
        x = self.stack.pop()
        if x == self.min[-1]:
            del self.min[-1]

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min[-1]