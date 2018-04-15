class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        # print(nums1)
        # print(nums2)
        l1 = len(nums1)
        l2 = len(nums2)

        if l1 < l2:
            l1, l2 = l2, l1
            nums1, nums2 = nums2, nums1

        m1 = l1 // 2
        m2 = l2 // 2

        if l2 <= 4:
            for i in range(l2):
                self.insert(nums1, nums2[i])
            #print(nums1)
            if (l1 + l2) % 2 == 1:
                return float(nums1[(l1 + l2) // 2])
            else:
                #print(1)
                return (nums1[(l1 + l2) // 2 - 1] + nums1[(l1 + l2 ) // 2]) / 2
            #print(1)

        if nums1[m1] > nums2[m2]:
            return(self.findMedianSortedArrays(nums1[ : l1 - m2 + 1], nums2[m2 - 1: ]))
        else:
            return(self.findMedianSortedArrays(nums1[l2 - m2 - 2:],nums2[ : m2 + 2] ))

    def insert(self, nums, a):
        """
        :type nums1: List[int]
        :type a: int
        :rtype: None
        """
        l = 0
        r = len(nums) - 1
        #print(nums, l, r, a)
        while l < r - 1:
            m = (l + r) // 2
            if nums[m] < a:
                l = m + 1
            elif nums[m] > a:
                r = m - 1
            else:
                #print(nums, l, r, a)
                nums.insert(m, a)
                return
        #print(nums, l, r, a)
        if l == r - 1:
            if a > nums[r]:
                nums.insert(r + 1, a)
            elif a > nums[l]:
                nums.insert(l + 1, a)
            else:
                nums.insert(l, a)
        else:
            if a > nums[l]:
                nums.insert(l + 1, a)
            else:
                nums.insert(l, a)
s = Solution()

nums1 = [3,3,3,3]
nums2 = [3,3,3,3]
print(s.findMedianSortedArrays(nums1, nums2))

# nums1 = [1, 3]
# nums2 = [2]
# print(s.findMedianSortedArrays(nums1, nums2))