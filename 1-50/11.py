class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ans = 0
        l = 0
        r = len(height) - 1
        while l < r:
            w = min(height[l], height[r])
            ans = max(ans, w * (r - l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return ans
s = Solution()
print(s.maxArea([2,3,4,1,2]))

