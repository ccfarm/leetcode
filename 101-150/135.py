class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        i = 0
        j = 1
        l = len(ratings)
        ans = 1
        now = 1
        while j < l:
            if ratings[j] > ratings[j-1]:
                now += 1
            elif ratings[j] == ratings[j-1]:
                now = 1
                i = j
            else:
                if now == 1:
                    ans += j - i
                else:
                    now = 1
                i = j
            ans += now
            j += 1
        return ans