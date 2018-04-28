# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        q = [root]
        ans = 1
        while q != []:
            tmp = []
            for i, node in enumerate(q):
                if node.left == None and node.right == None:
                    return ans
                else:
                    if node.left != None:
                        tmp.append(node.left)
                    if node.right != None:
                        tmp.append(node.right)
            q = tmp.copy()
            tmp.clear()
            ans += 1