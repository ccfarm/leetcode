# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        l1 = head
        while True:
            while l1.next != None and l1.val != l1.next.val:
                l1 = l1.next
            if l1.next == None:
                return head
            l2 = l1.next
            while l2 != None and l2.val == l1.val:
                l2 = l2.next
            l1.next = l2
            if l2 == None:
                return head