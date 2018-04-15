class Solution:
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(graph)
        path = [[] for _ in range(n)]
        path[0].append([0])
        for i in range(n - 1):
            for l in path[i]:
                for k in graph[i]:
                    path[k].append(l + [k])
        return path[n - 1]