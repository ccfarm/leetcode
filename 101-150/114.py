# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        def f(root):
            first = last = root
            r = root.right
            if root.left != None:
                l1, l2 = f(root.left)
                root.right = l1
                l2.right = r
                last = l2
            if r != None:
                last = f(root.right)[1]
            return first, last
        f(root)