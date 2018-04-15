class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        l = [ListNode(0) for x in range(k + 2)]
        link = head
        for i in range(1, k + 1):
            l[i] = link
            if link == None:
                return head
            link = link.next
        l[k + 1] = link
        head = l[k]
        for i in reversed(range(2,k + 1)):
            l[i].next = l[i - 1]
        l[1].next = l[k + 1]

        while 1:
            l[0] = l[1]
            for i in range(1, k + 1):
                l[i] = l[k + 1]
                if l[k + 1] == None:
                    return head
                l[k + 1] = l[k + 1].next
            l[0].next = l[k]
            for i in reversed(range(2, k + 1)):
                l[i].next = l[i - 1]
            l[1].next = l[k + 1]