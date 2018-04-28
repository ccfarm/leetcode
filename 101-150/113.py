# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        tmp = []
        ans = []
        def dfs(root, sum):
            sum -= root.val
            tmp.append(root.val)
            if root.left == None and root.right == None and sum == 0:
                ans.append(tmp.copy())
            else:
                if root.left != None:
                    dfs(root.left, sum)
                if root.right != None:
                    dfs(root.right, sum)
            tmp.pop()
            sum += root.val
        if root == None:
            return []
        else:
            dfs(root)
            return ans