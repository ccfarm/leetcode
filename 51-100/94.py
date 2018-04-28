# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        def dfs(node):
            if node.left != None:
                dfs(node.left)
            ans.append(node.val)
            if node.right != None:
                dfs(node.right)
        if root == None:
            return []
        dfs(root)
        return ans