# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        for i in reversed(range(len(lists))):
            if lists[i] == None:
                del lists[i]
        if lists == []:
            return None
        self.qsort(lists, 0, len(lists) - 1)
        link = head = lists[0]
        if lists[0].next == None:
            del lists[0]
        else:
            lists[0] = lists[0].next
            self.isort(lists)
        while len(lists) > 0:
            link.next = lists[0]
            link = link.next
            if lists[0].next == None:
                del lists[0]
            else:
                lists[0] = lists[0].next
                self.isort(lists)
        return head

    def qsort(self, lists, ll, rr):
        x = lists[ll]
        l = ll
        r = rr
        while l < r:
            while l < r and lists[r].val >= x.val:
                r -= 1
            if l < r:
                lists[l] = lists[r]
                l += 1
            while l < r and lists[l].val <= x.val:
                l += 1
            if l < r:
                lists[r] = lists[l]
                r -= 1
        lists[l] = x
        r -= 1
        l += 1
        if ll < r:
            self.qsort(lists, ll, r)
        if l < rr:
            self.qsort(lists, l, rr)

    def isort(self, lists):
            x = lists[0]
            del lists[0]
            i = 0
            while i < len(lists) and x.val > lists[i].val:
                i += 1
            lists.insert(i, x)



