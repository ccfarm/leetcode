# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        p = [root]
        ans = []
        flag = False
        while p != []:
            q1 = []
            q2 = []
            for node in p:
                q1.append(node.val)
                if node.left != None:
                    q2.append(node.left)
                if node.right != None:
                    q2.append(node.right)
            if flag:
                q1.reverse()
            flag = not flag
            ans.append(q1)
            p = q2
        return ans