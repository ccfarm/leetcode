class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        dis = 2 ** 32
        for i in range(n - 2):
            j = i + 1
            k = n - 1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if abs(sum - target) < dis:
                    dis = abs(sum - target)
                    ans = sum
                if sum > target:
                    k -= 1
                elif sum < target:
                    j +=1
                else:
                    return target
        return ans
