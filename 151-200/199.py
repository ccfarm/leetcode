# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        p = [root]
        ans = []
        while p:
            ans.append(p[-1].val)
            q = []
            for x in p:
                if x.left != None:
                    q.append(x.left)
                if x.right != None:
                    q.append(x.right)
            p = q
        return ans