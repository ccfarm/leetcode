class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        l = ['(', '{', '[']
        r = [')', '}', ']']
        for i in range(len(s)):
            if s[i] in l:
                stack.append(s[i])
            else:
                if len(stack) == 0:
                    return False
                else:
                    if s[i] == ')':
                        if stack.pop() != '(':
                            return False
                    elif s[i] == '}':
                        if stack.pop() != '{':
                            return False
                    elif s[i] == ']':
                        if stack.pop() != '[':
                            return False
        return len(stack) == 0