"""

Given a 0-indexed integer array nums, return true if it can be made strictly increasing after removing exactly one element, or false otherwise. If the array is already strictly increasing, return true.

The array nums is strictly increasing if nums[i - 1] < nums[i] for each index (1 <= i < nums.length).

 

Example 1:

Input: nums = [1,2,10,5,7]
Output: true
Explanation: By removing 10 at index 2 from nums, it becomes [1,2,5,7].
[1,2,5,7] is strictly increasing, so return true.
Example 2:

Input: nums = [2,3,1,2]
Output: false
Explanation:
[3,1,2] is the result of removing the element at index 0.
[2,1,2] is the result of removing the element at index 1.
[2,3,2] is the result of removing the element at index 2.
[2,3,1] is the result of removing the element at index 3.
No resulting array is strictly increasing, so return false.
Example 3:

Input: nums = [1,1,1]
Output: false
Explanation: The result of removing any element is [1,1].
[1,1] is not strictly increasing, so return false.
Example 4:

Input: nums = [1,2,3]
Output: true
Explanation: [1,2,3] is already strictly increasing, so return true.
 

Constraints:

2 <= nums.length <= 1000
1 <= nums[i] <= 1000

"""

class Solution(object):
    def canBeIncreasing(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        index = -1
        count = 0
        
        n = len(nums)
        
        # count the number of non-decreasing elements
        for i in range(n-1):
            if nums[i] >= nums[i+1]:
                index = i
                count += 1
                
        # all strictly increasing        
        if count == 0:
            return True
        
        
        # only one non-decreasing element
        if count == 1:
            # just need to remove one element
            if index == 0 or index == n - 2:
                return True
            
            if nums[index-1] < nums[index+ 1] or (index+2 < n and nums[index] < nums[index+2]):
                return True
            
            
        return False
        
        
        
        
        
        
        
        
        
        
        
