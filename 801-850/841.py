class Solution:
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        n = len(rooms) + 1
        q = rooms[0]
        s = set([0])
        while q:
            x = q.pop()
            if x not in s:
                s.add(x)
                for y in rooms[x]:
                    if y not in s:
                        s.add(y)
        l = len(s)
        return l == n
