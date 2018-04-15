class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = {}
        ans = []
        index = 0
        for i in range(len(strs)):
            str = strs[i]
            l = list(str)
            l.sort()
            t = tuple(l)
            if t not in d:
                d[t] = index
                ans.append([str])
                index += 1
            else:
                ans[d[t]].append(str)
        return ans