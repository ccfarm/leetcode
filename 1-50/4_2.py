    # refer to https://leetcode.com/problems/median-of-two-sorted-arrays/solution/

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)

        if m > n:
            m, n = n, m
            A, B = nums2, nums1
        else:
            A, B = nums1, nums2

        l = 0
        r = m

        while l <= r:
            i = (l + r) // 2
            j = (m + n + 1) // 2 - i
            # print(l, r)
            # print(i, j)
            if (i < m) and (A[i] < B[j - 1]):
                l = i + 1
            elif (i > 0) and (A[i - 1] > B[j]):
                r = i - 1
            else:
                if (m + n) % 2 == 0:
                    ans1 = -999999;
                    if i > 0:
                        ans1 = max(ans1, A[i - 1])
                    if j > 0:
                        ans1 = max(ans1, B[j - 1])
                    ans2 = 999999;
                    if i < m:
                        ans2 = min(ans2, A[i])
                    if j < n:
                        ans2 = min(ans2, B[j])
                    #print (ans1, ans2)
                    return (ans1 + ans2) / 2
                else:
                    ans = -999999;
                    if i > 0:
                        ans = max(ans, A[i - 1])
                    if j > 0:
                        ans = max(ans, B[j - 1])
                    return ans

s = Solution()

nums1 = [1,2]
nums2 = [1,2]
print(s.findMedianSortedArrays(nums1, nums2))


