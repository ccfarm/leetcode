# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        d = {}
        def dfs(node):
            new = UndirectedGraphNode(node.label)
            d[new.label] = new
            for x in node.neighbors:
                if x.label not in d:
                    dfs(x)
                new.neighbors.append(d[x.label])
            return new
        ans = dfs(node)
        return ans
