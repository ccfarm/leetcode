# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        a = l1.val + l2.val
        b = a % 10
        a = a // 10
        ans = ListNode(b)
        if l1 != None:
            l1 = l1.next
        if l2 != None:
            l2 = l2.next
        if (l1 != None) or (l2 != None) or (a != 0):
            ans.next = self.add(l1, l2, a)
        else:
            ans.next = None
        return ans

    def add(self, l1, l2, aa):
        """
        :type l1: ListNode
        :type l2: ListNode
        :type a: int
        :rtype: ListNode
        """
        b = self.get(l1)
        c = self.get(l2)
        a = b + c + aa
        b = a % 10
        a = a // 10
        ans = ListNode(b)
        if l1 != None:
            l1 = l1.next
        if l2 != None:
            l2 = l2.next
        if (l1 != None) or (l2 != None) or (a != 0):
            ans.next = self.add(l1, l2, a)
        else:
            ans.next = None
        return ans

    def get(self,l):
        """
        :type l: ListNode
        """
        if (l == None):
            return 0
        else:
            return l.val

a = ListNode(2)
a.next = ListNode(4)
a.next.next = ListNode(3)
b = ListNode(5)
b.next = ListNode(6)
b.next.next = ListNode(4)
s = Solution()
print(s.addTwoNumbers(a,b).val)