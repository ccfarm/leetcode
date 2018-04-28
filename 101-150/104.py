# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0
        def dfs(root, d):
            self.ans = max(self.ans, d)
            if root.left != None:
                dfs(root.left, d + 1)
            if root.right != None:
                dfs(root.right, d + 1)
        if root != None:
            dfs(root, 1)
        return self.ans