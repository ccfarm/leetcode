class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        pre = ListNode(0)
        pre.next = head
        l1 = pre
        l2 = pre
        while l2 != None:
            l1 = l1.next
            l2 = l2.next
            if l2 !=None:
                l2 = l2.next
            else:
                return False
            if l1 == l2:
                return True
        else:
            return False
