# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if head == None:
            return None
        n = 0
        l = []
        link = head
        d = {}
        while link:
            node = RandomListNode(link.label)
            l.append(node)
            d[link.label] = node
            link = link.next
            n += 1
        link = head
        for i,x in enumerate(l):
            if i < n - 1:
                x.next = l[i+1]
            if link.random != None:
                x.random = d.get(link.random.label)
            link = link.next
        return l[0]