class Solution:
    def numSimilarGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        n = len(A)
        if n == 0:
            return 0
        l = len(A[0])
        d = {}
        for i in range(n):
            for j in range(i+1, n):
                count = 0
                for k in range(l):
                    if A[i][k] == A[j][k]:
                        count += 1
                if count == 2:
                    d[i] = d.get(i, []) + [j]
                    d[j] = d.get(j, []) + [i]
        s = set()
        ans = 0
        for i in range(n):
            if i not in s:
                ans += 1
                q = [i]
                while q:
                    x = q.pop()
                    if x in s:
                        continue
                    s.add(x)
                    for y in d.get(x, []):
                        if y not in s:
                            q.append(y)

        return ans
