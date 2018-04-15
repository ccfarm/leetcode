class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        arr = [-1 for x in range(128)]
        maxx = 0
        now = 0
        for i in range(len(s)):
            now += 1
            if arr[ord(s[i])] > -1:
                now = min(now, i - arr[ord(s[i])])
                maxx = max(maxx, now)
            arr[ord(s[i])] = i
            maxx = max(maxx, now)
        return maxx

a = Solution
print(a.lengthOfLongestSubstring(a, "pwwkew"))