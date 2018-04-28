# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if inorder == []:
            return None
        x = postorder[-1]
        l = inorder.index(x)
        root = TreeNode(x)
        root.left = self.buildTree(inorder[:l], postorder[:l])
        root.right = self.buildTree(inorder[l+1:], postorder[l:-1])
        return root