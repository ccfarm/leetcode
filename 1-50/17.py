class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        chrs = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        ans = []
        def re(st, remains):
            """
            :type st: str
            :type: remains: str
            """
            if remains == "":
                ans.append(st)
            else:
                dig = int(remains[0])
                for i in range(len(chrs[dig])):
                    re(st + chrs[dig][i], remains[1:])
        re("", digits)
        return ans
s = Solution()
print(s.letterCombinations("23"))