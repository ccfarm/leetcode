class Solution:
    def flipgame(self, fronts, backs):
        """
        :type fronts: List[int]
        :type backs: List[int]
        :rtype: int
        """
        n = len(fronts)
        d = {}
        for i in range(n):
            if fronts[i] not in d:
                d[fronts[i]] = [i]
            else:
                d[fronts[i]].append(i)
            if backs[i] not in d:
                d[backs[i]] = [i]
            else:
                d[backs[i]].append(i)
        for i in range(1, 2001):
            if i in d:
                for x in d[i]:
                    if d[i].count(x) == 1:
                        return i
        return 0