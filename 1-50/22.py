class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        st = []
        ans = []
        def bt(n, m):
            if m == 0:
                ans.append(''.join(st))
                return
            else:
                if n > 0:
                    st.append('(')
                    bt(n - 1, m)
                    st.pop()
                if n < m:
                    st.append(')')
                    bt(n, m - 1)
                    st.pop()
        bt(n, n)
        return ans
s = Solution()
print(s.generateParenthesis(3))