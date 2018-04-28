class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = len(s)
        if l == 0:
            return 0

        dp = [0] * l
        if s[0] != 0:
            dp[0] = 1
        if s[1] != '0':
            dp[1] += 1
        if l >= 2 and int(s[0:2]) <=26:
            dp[1] += dp[0]

        for i in range(2, l):
            if s[i] != '0':
                dp[i] += dp[i-1]
            if i + 2 <= l and int(s[i:i+2]) <= 26:
                dp[i] += dp[i-2]
        print(dp[i-1])