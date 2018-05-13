# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.l = [root]
        while self.l[-1].left != None:
            self.l.append(l[-1].left)

    def hasNext(self):
        """
        :rtype: bool
        """
        return (self.l != [])

    def next(self):
        """
        :rtype: int
        """
        x = self.l[-1]
        x = x.right
        while x != None:
            self.l.append(x)
            x = x.left
        return x.val

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())