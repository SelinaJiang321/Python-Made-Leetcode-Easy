"""

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.

"""

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        pos = 0
        
        # swap the elements(non-zero and zero) in the array 
        # keep track of the position where the non-zero element can be swapped in
        for i in range(len(nums)):
            elem =  nums[i]
            if elem != 0:
                nums[i] , nums[pos] = nums[pos] , nums[i]
                pos += 1
                
        # Any comments?
         
