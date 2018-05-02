class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        l = len(gas)
        a = []
        for i in range(l):
            a.append(gas[i] - cost[i])
        i = 0
        j = 0
        remain = a[0]
        while (j + 1) % l == i:
            if remain + a[j+1] >= 0:
                j += 1
                remain += a[j]
            else:
                while (j + 1) % l != i and remain + a[j+1] < 0:
                    i = (i - 1) % l
                    remain += a[i]
        if remain >= 0:
            return i
        else:
            return -1