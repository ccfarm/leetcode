# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if root == None:
            return
        q = [root]
        while q != []:
            temp = []
            l = len(q)
            for i,x in enumerate(q):
                if x.left != None:
                    temp.append(x.left)
                if x.right != None:
                    temp.append(x.right)
                if i < l-1:
                    x.next = q[i+1]
            q = temp.copy()