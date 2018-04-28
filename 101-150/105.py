# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if preorder == []:
            return None
        x = preorder.val
        l = inorder.index(x)
        root = TreeNode(x)
        root.left = self.buildTree(preorder[1:1+l], inorder[:l])
        root.right = self.buildTree(preorder[l+1:], inorder[l+1:])
        return root