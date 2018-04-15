# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        l1 = head
        l2 = l1.next
        if l2 == None:
            return head
        if l2.next == None:
            l1.next = None
            l2.next = l1
            return l2
        l3 = l2.next
        head = l2
        head.next = l1
        l1.next = l3
        l2 = l3
        l3 = l3.next
        if l3 == None:
            return head
        l4 = l3.next
        while 1:
            l1.next = l3
            l3.next = l2
            l2.next = l4
            if l4 == None:
                return head
            else:
                l1 = l2
                l2 = l4
                l3 = l4.next
                if l3 == None:
                    return head
                l4 = l3.next

