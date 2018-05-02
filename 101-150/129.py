# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0
        def dfs(root, now):
            now = now * 10 + root.val
            if root.left == None and root.right == None:
                self.ans += now
            else:
                if root.left != None:
                    dfs(root.left, now)
                if root.right != None:
                    dfs(root.right, now)
        if root != None:
            dfs(root, 0)
        return self.ans