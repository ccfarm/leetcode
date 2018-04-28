# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        q = [root]
        while q != None:
            p = []
            for node in q:
                if node != None:
                    p.append(node.left)
                    p.append(node.right)
            i = 0
            j = len(p) - 1
            while i < j:
                if p[i] != p[j]:
                    return False
                i += 1
                j -= 1
            q = p
        return True