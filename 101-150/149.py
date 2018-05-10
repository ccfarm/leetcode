class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution:
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        ans = 0
        l = len(points)
        for i in range(l):
            same = 1
            d = {}
            for j in range(l):
                if points[j].x == points[i].x and points[j].y == points[i].y:
                    same += 1
                    continue
                if points[j].x == points[i].x:
                    d['i'] = d.get('i', 0) + 1
                else:
                    slop = (points[j].y - points[i].y) / (points[j].x - points[i].x)
                    d[slop] = d.get(slop, 0) + 1
            ans = max(ans, max(d.values()) + same)
        return ans