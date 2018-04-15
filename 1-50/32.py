class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = len(s)
        stack = []
        for i in range(l):
            if s[i] == '(':
                stack.append(i)
            else:
                if len(stack) == 0 or s[stack[-1]] != '(':
                    stack.append(i)
                else:
                    del stack[-1]

        if len(stack) == 0:
            return l
        else:
            ans = max(stack[0], l - stack[-1] - 1)
            if len(stack) >= 2:
                for i in range(len(stack) - 1):
                    ans = max(ans, stack[i + 1] - stack[i] - 1)
            return ans


s = Solution()
print(s.longestValidParentheses(")(((((()())()()))()(()))("))
