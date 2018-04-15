# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None:
            return head
        if k == 0:
            return head
        l1 = l2 = head
        for i in range(k):
            l2 = l2.next
        if l2 != None:
            while l2.next != None:
                l1 = l1.next
                l2 = l2.next
            l2.next = head
            head = l1.next
            l1.next = None
        return head
