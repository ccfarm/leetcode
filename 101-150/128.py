class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = set()
        for x in nums:
            s.add(x)
        ans = 0
        for x in nums:
            if x in s:
                s.remove(x)
                now = 1;
                l = x-1
                while l in s:
                    s.remove(l)
                    now += 1
                    l -= 1
                r = x + 1
                while r in s:
                    s.remove(r)
                    now += 1
                    r += 1
            ans = max(ans, now)
        return ans