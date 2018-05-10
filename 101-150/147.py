class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = ListNode(0)
        pre.next = head
        l1 = pre.next
        if l1 == None:
            return pre.next
        while l1.next != None:
            l0 = l1
            l1 = l1.next
            l2 = pre.next
            l3 = pre
            while l2 != l1 and l2.val <= l1.val:
                l2 = l2.next
                l3 = l3.next
            if l2 != l1:
                l3.next = l1
                l0 = l1.next
                l1.next = l2


