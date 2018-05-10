import queue
class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = queue.LifoQueue()
        for x in tokens:
            if x.isDigits():
                stack.put(int(x))
            else:
                a = stack.get()
                b = stack.get()
                if x == "+":
                    c = a + b
                elif x == "-":
                    c = a - b
                elif x == "*":
                    c = a * b
                elif x == "/":
                    c = a // b
                stack.put(c)
        return stack.get()
