# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        h1 = None
        h2 = None
        l1 = None
        l2 = None
        now = head
        while now != None:
            if now.val < x:
                if h1 != None:
                    l1.next = now
                    l1 = l1.next
                else:
                    h1 = l1 = now
            else:
                if h2 != None:
                    l2.next = now
                    l2 =l2.next
                else:
                    h2 = l2 = now
            now = now.next
        if l1 != None:
            l1.next = h2
            if l2 != None:
                l2.next = None
            return h1
        else:
            return h2