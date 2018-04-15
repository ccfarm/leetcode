import heapq
class Solution:
    def racecar(self, target):
        """
        :type target: int
        :rtype: int
        """
        K = target.bit_length() + 1
        barrier = 1 << k
        dist = [float('inf')] * (barrier * 2 + 1)
        dist[0] = 0
        pq = [(0, 0)]

        while pq:
            step, loc = heapq.heappop(pq)
            for k in range(K + 1):
                walk = 1 << k - 1
                step2 = step + walk + 1
                loc2 = walk - loc
                if loc2 == target:
                    return step2 - 1
                elif abs(loc2) < barrier and step2 < dist[loc2]:
                    dist[loc2] = step2
                    heapq.heappush(pq, (step2, loc2))