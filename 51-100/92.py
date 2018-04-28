class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummyNode = ListNode(0)
        l1 = dummyNode
        for i in range(m - 1):
            l1 = l1.next
        l2 = l1.next
        l3 = None
        for j in range(n - m):
            l4 = l2.next
            l2.next = l3
            l3 = l2
            l2 = l4
        l1.next.next = l4
        l1.next = l3
        return dummyNode.next