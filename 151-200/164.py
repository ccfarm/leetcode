class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if l <= 1:
            return 0
        c1 = 2 ** 32
        min_num =c1
        max_num = -c1
        for x in nums:
            min_num = min(min_num, x)
            max_num = max(max_num, x)
        w = (max_num - min_num) / (l - 1)
        bucket = [[c1, -c1] for _ in range(l)]
        for x in nums:
            index = round((x - min_num) / w)
            bucket[index][0] = min(bucket[index][0], x)
            bucket[index][1] = max(bucket[index][1], x)
        ans = 0
        i = 0
        while i < len(bucket)-1:
            if bucket[i][0] == c1:
                del bucket[i]
            elif bucket[i+1][0] == c1:
                del bucket[i+1]
            else:
                ans = max(ans, bucket[i+1][0]-bucket[i][1])
                i += 1
        return ans
