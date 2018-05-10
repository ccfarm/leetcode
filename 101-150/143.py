# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        a = []
        while head != None:
            a.append(head)
            head = head.next
        i = 0
        j = len(a) - 1
        dummy = ListNode(0)
        pre = dummy
        while i < j:
            pre.next = a[i]
            pre = pre.next
            pre.next = a[j]
            i += 1
            j -= 1
        if i == j:
            pre.next = a[i]
        return dummy.next
