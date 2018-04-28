# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def f(root):
            if root == None:
                return 0, True
            d = 1
            b = True
            l1, l2 = f(root.left)
            r1, r2 = f(root.right)
            if abs(l1 - l2) > 1:
                b = False
            b = b and l2 and r2
            d = 1 + max(l1, l2)
            return d, b

        return f(root)[1]
