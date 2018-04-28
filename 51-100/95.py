class Solution:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """

        def dfs(l, r):
            re = []
            for i in range(l, r + 1):
                left = dfs(l, i - 1)
                right = dfs(i + 1, r)
                for k1 in left:
                    for k2 in right:
                        root = TreeNode(i)
                        root.left = k1
                        root.right = k2
                        re.append(root)
            if re == []:
                re.append(None)
            return re

        if n == 0:
            return []
        return dfs(1, n)
