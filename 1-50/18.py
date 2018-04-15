class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        n = len(nums)
        ans = []
        s = set([])
        for i in range(n - 3):
            for j in range(i + 1, n - 2):
                k = j + 1
                l = n - 1
                while k < l:
                    sum = nums[i] + nums[j] + nums[k] + nums[l]
                    if sum == target:
                        st = str(nums[i])+ str(nums[j]) + str(nums[k]) + str(nums[l])
                        if st not in s:
                            s.add(st)
                            ans.append([nums[i], nums[j], nums[k], nums[l]])
                    if sum > target:
                        l -= 1
                    elif sum < target:
                        k += 1
                    else:
                        l -= 1
                        k += 1
        return ans