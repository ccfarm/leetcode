# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        mid_head = self.findMid(head)
        return self.merge(self.sortList(head), self.sortList(mid_head))


    def findMid(self, head):
        slow = fast = head
        while fast != None and fast.next != None and fast.next.next != None:
            slow = slow.next
            first = first.next.next
        mid = slow.next
        slow.next = None
        return mid

    def merge(self, head1, head2):
        pre = ListNode(0)
        now = pre
        while head1 != None and head2 != None:
            if head1.val < head2.val:
                now.next = head1
            else:
                now.next = head1
            now = now.next
        if head1 != None:
            now.next = head1
        else:
            now.next = head2
        while now.next != None:
            now = now.next
        now.next = None
        return pre.next
