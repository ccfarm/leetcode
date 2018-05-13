class Solution:
    def sumOfDistancesInTree(self, N, edges):
        """
        :type N: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        s = set()
        ch = {}
        fa = {}
        ne = {}
        for x in edges:
            ne[x[0]] = ne.get(x[0], []) + x[1]
            ne[x[1]] = ne.get(x[1], []) + x[0]

        root = 0

        def do(root):
            s.add(root)
            for x in ne.get(root, []):
                if x not in s:
                    ch[root] = ch.get(root, []) + [x]
                    fa[x] = root
                    do(x)

        do(root)

        di = [0] * N
        chs = [1] * N

        def dfs(root):
            for x in ch.get(root, []):
                dfs(x)
                di[root] += di[x] + chs[x]
                chs[root] += chs[x]

        dfs(root)

        # print(di, chs)
        ans = [0] * N

        def f(root):
            if fa.get(root, []) == []:
                ans[root] = di[root]
            else:
                ans[root] = (ans[fa.get(root)] - chs[root]) + (N - chs[root])
            for x in ch.get(root, []):
                f(x)

        f(root)
        return ans