class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = len(height)
        maxx = 0
        left = []
        for i in range(l):
            left.append(maxx)
            maxx = max(maxx, height[i])
        maxx = 0
        right = []
        for i in reversed(range(l)):
            right.insert(0, maxx)
            maxx = max(maxx, height[i])
        ans = 0
        for i in range(l):
            minn = min(left[i], right[i])
            if minn > height[i]:
                ans += minn - height[i]
        return ans