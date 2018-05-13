class Solution:
    def findReplaceString(self, S, indexes, sources, targets):
        """
        :type S: str
        :type indexes: List[int]
        :type sources: List[str]
        :type targets: List[str]
        :rtype: str
        """
        l = len(S)
        mark = [-1] * l
        l2 = len(indexes)
        i = 0
        while i < l2:
            index = indexes[i]
            l3 = len(sources[i])
            if index + l3 <= l and S[index:index + l3] == sources[i]:
                for j in range(index, index + l3):
                    mark[j] = i
                i = indexes + l3
            else:
                i+= 1
        ans = ''
        i=0
        while i < l2:
            if l[i] == -1:
                ans = ans + S[i]
                i+=1
            else:
                x = l[i]
                ans = ans + targets[x]
                while i < l2 and l[i] == x:
                    i += 1
        return ans
