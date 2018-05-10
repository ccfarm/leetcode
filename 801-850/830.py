class Solution(object):
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        i, j = 0, 1
        l = len(s)
        ans = []
        while j < l:
            if s[j] == s[i]:
                j += 1
            else:
                if j - i >= 3:
                    ans.append(i, j-1)
                i = j
                j += 1
        if j - i >= 3:
            ans.append(i, j - 1)
        i = j
        j += 1
        return ans
