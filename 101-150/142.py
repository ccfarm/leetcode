# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = ListNode(0)
        pre.next = head
        l1 = pre
        l2 = pre
        while l2 != None:
            l1 = l1.next
            l2 = l2.next
            if l2 != None:
                l2 = l2.next
            else:
                return None
            if l1 == l2:
                break
        else:
            return None

        l1 = l2
        l = 1
        l2 = l2.next
        while l2 != l1:
            l2 = l2.next
            l += 1
        l1 = l2 = pre
        while l > 0:
            l2 = l2.next
            l -= 1
        while l1 != l2:
            l1 = l1.next
            l2 = l2.next
        return l1