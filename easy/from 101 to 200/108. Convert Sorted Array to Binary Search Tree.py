"""

Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        
        center = 0
        
        # outside if: len(nums) == 0
        if 0 <= center < len(nums):
            center = len(nums) // 2
            value = nums[center]
            # construct a root
            root = TreeNode(value)
            # slicing :left except from the center
            #          right starts from center + 1
            root.left = self.sortedArrayToBST(nums[:center])
            root.right = self.sortedArrayToBST(nums[center+1::])
            return root
        
        return None
        
        # Any comments?
        
