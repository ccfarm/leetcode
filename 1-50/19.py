# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        l1 = head
        l2 = head
        for i in range(n):
            l2 = l2.next
        if l2 != None:
            while l2.next != None:
                l1 = l1.next
                l2 = l2.next
            l1.next = l1.next.next
        else:
            head = head.next
        return head