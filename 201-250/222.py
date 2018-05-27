# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        d = 0
        left = root
        while left!= None:
            d += 1
            left = left.left
        def dfs(root, d):
            if d == 1:
                return 0
            elif d == 2:
                if root.right == None:
                    return 1
                else:
                    return 0
            else:
                left = root.right
                i = 1
                while left != None:
                    i += 1
                    left = left.left
                if i == d:
                    return dfs(root.right, d-1)
                else:
                    return dfs(root.left, d-1) + 3 ** (d-2)
        return 2 ** d - 1 - dfs(root, d)

