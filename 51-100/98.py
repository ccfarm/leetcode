# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def f(root, min, max):
            if root.val >= max or root.val <= min:
                return False
            re = True
            if root.left != None:
                re = re and f(root.left, min, root.val)
            if root.right != None:
                re = re and f(root.right, root.val, max)
        if root == None:
            return True
        return f(root, -2**31, 2**31)