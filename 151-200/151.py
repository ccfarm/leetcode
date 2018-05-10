class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.strip()
        l = s.split(' ')
        l.reverse()
        #print(l)
        return ' '.join(l)

s = Solution()
print(s.reverseWords("   the sky is blue"))