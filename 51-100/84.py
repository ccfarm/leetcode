class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if heights == []:
            return 0
        ans = 0
        stack = []
        for i,x in enumerate(heights):
            if stack == [] and x > heights[stack[-1]]:
                stack.append(i)
            else:
                while stack != [] and x <= heights[stack[-1]]:
                    min = heights[stack.pop()]
                    if stack == []:
                        l = -1
                    else:
                        l = stack[-1]
                    r = i
                    ans = max(ans, (r - l - 1) * min)
                stack.append(i)
        while stack != []:
            min = heights[stack.pop()]
            if stack == []:
                l = -1
            else:
                l = stack[-1]
            r = len(heights)
            ans = max(ans, (r - l - 1) * min)
        return ans