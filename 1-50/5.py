#reference: https://www.cnblogs.com/grandyang/p/4475985.html

class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = '#' + '#'.join(list(s)) + '#'
        l = len(s)
        p = [1 for x in range(l)]
        mx = 0
        id = 0
        ans = 0
        loc = 0
        for i in range(l):
            if mx > i:
                j = 2 * id - i
                p[i] = min(mx - i, p[j])
            else:
                p[i] = 1
            kr = i + p[i]
            kl = i - p[i]
            #print(i, p[i])
            while kr < l and kl >= 0:
                if s[kr] == s[kl]:
                    p[i] += 1
                    kr += 1
                    kl -= 1
                else:
                    break
            if i + p[i] > mx:
                mx = i + p[i]
                id = i
            if (ans < p[i]):
                ans = p[i]
                loc = i
        str = s[loc - ans + 1: loc + ans].replace('#', '')
        return str

s = Solution()
print(s.longestPalindrome("abcdcba"))
print(s.longestPalindrome("abcdcba"))
print(s.longestPalindrome("cbbd"))




