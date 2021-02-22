"""

A peak element is an element that is strictly greater than its neighbors.

Given an integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞.

 

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.
 

Constraints:

1 <= nums.length <= 1000
-231 <= nums[i] <= 231 - 1
nums[i] != nums[i + 1] for all valid i.

"""

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # no elements:
        if len(nums) == 1: return 0
        if len(nums) == 2:
            if nums[0] > nums[1] : return 0
            else: return 1
       
        for i in range(1,len(nums) - 1, 1):
            if nums[0] > nums[i]: return 0
            if (nums[i] > nums[i - 1]) and (nums[i] > nums[i+1]):
                return i
        if nums[len(nums) - 1] > nums[i]: return len(nums)- 1
        
        # Time Complexity: O (n)
        # Space Complexity: O (1)
        
        # Any comments?
        
