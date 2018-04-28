# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.first = None
        self.second = None
        self.pre = None
        def dfs(root):
            if root.left == None:
                if self.pre != None and self.pre.val > root:
                    if self.first == None:
                        self.first = self.pre
                        self.second = root
                    else:
                        self.second = root
            else:
                dfs(root.left)
                if self.pre.val > root:
                    if self.first == None:
                        self.first = self.pre
                        self.second = root
                    else:
                        self.second = root
            self.pre = root
            if root.right != None:
                dfs(root.right)



        dfs(root)
        #print(self.first.val, self.second.val)
        self.first.val, self.second.val = self.second.val, self.first.val