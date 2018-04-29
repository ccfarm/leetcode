class Solution:
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        # l = [[0] * 121 for _ in range(121)]
        # for i in range(1,121):
        #     start = i // 2 + 7
        #     for j in range(start, i + 1):
        #         l[i,j] = 1
        ans = 0
        l2 = [0] * 121
        for x in ages:
            l2[x] += 1
        for i in range(1,121):
            start = i // 2 + 7
            count = l2[i]
            temp = 0
            if count > 0:
                for j in range(start, i+1):
                    if i == j:
                        temp += (l2[j] - 1)
                    else:
                        temp += l2[j]
            ans += count * temp
        return ans
