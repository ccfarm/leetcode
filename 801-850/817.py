# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        d = {}
        link = head
        while link != None:
            d[link.val] = link
            link = link.next
        s = set(G)
        count = 0
        link = head
        while link != None:
            i = link.val
            if i in s:
                count += 1
                s.remove(i)
                if d[i].next != None:
                    i = d[i].next.val
                    while i in s:
                        s.remove(i)
                        i = d[i].next
        return count