# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        l1 = head
        l2 = head.next
        while l1.val == l2.val:
            l2 = l2.next
            while l2 != None and l2.val == l1.val:
                l2 = l2.next
            head = l2
            if head == None or head.next == None:
                return head
            l1 = head
            l2 = head.next
        while 1:
            while l2.next != None and l2.val != l2.next.val:
                l1 = l2
                l2 = l2.next
            if l2.next == None:
                return head
            while l2.next != None and l2.val == l2.next.val:
                l2 = l2.next
            if l2.next == None:
                return head
            l1.next = l2.next
            l2 = l2.next

