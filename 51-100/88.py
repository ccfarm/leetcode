class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        l = m - n
        for i in range(n):
            j = 0
            while j < l and nums2[i] > nums1[j]:
                j += 1
            for k in reversed(range(j, l)):
                nums1[k + 1] = nums1[k]
            nums1[j] = nums2[i]


