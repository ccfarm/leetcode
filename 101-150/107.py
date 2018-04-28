# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans = []
        if root == None:
            return []
        queue = [root]
        level = []
        tmp = []
        while queue != []:
            for node in queue:
                level.append(node.val)
                if node.left != None:
                    tmp.append(node.left)
                if node.right != None:
                    tmp.append(node.right)
            queue = tmp
            tmp = []
            level = []
            ans.insert(0, level.copy())
        return ans