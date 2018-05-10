class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        l1 = 0
        l2 = 0
        link1 = headA
        link2 = headB
        while l1 != None:
            link1 = link1.next
            l1 += 1
        while l2 != None:
            link2 = link2.next()
            l2 += 1
        if l1 < l2:
            l1, l2 = l2, l1
            headA, headB = headB, headA
        link1 = headA
        link2 = headB
        while l1 > l2:
            link1 = link1.next
            l1 -= 1
        while link1 != None:
            if link1 == link2:
                return link1
            link1 = link1.next
            link2 = link2.next
        return None

