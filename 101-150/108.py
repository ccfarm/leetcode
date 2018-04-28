# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        l = len(nums)
        if l == 0:
            return None
        else:
            m = (l + 1) // 2
            root = TreeNode(nums[m])
            root.left = self.sortedArrayToBST(nums[:m])
            root.right = self.sortedArrayToBST(nums[m+1:])
            return root