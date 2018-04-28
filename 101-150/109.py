# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if head == None:
            return None
        pre = ListNode(0)
        pre.next = head
        l1 = l2 = pre
        while True:
            if l2.next != None and l2.next.next != None:
                l2 = l2.next.next
                l1 = l1.next
            else:
                break
        l2 = l1.next
        root = TreeNode(l2.val)
        l1.next = None
        root.left = self.sortedListToBST(pre.next)
        root.right = self.sortedListToBST(l2.next)
        return root

