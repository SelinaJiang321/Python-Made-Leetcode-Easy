"""

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Example 2:

Input: nums = [1]
Output: 1
Example 3:

Input: nums = [0]
Output: 0
Example 4:

Input: nums = [-1]
Output: -1
Example 5:

Input: nums = [-100000]
Output: -100000
 

Constraints:

1 <= nums.length <= 3 * 104
-105 <= nums[i] <= 105
 

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.


"""

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        maxsum = nums[0]
        curr_sum = 0
        
        for n in nums:
            # if the prefix is smaller than 0 then there's no point adding it
            if curr_sum < 0:
                curr_sum = 0
                curr_sum += n
            maxsum = max(maxsum, curr_sum)
        return maxsum
        
        """
        Time Complexity: O(1) linear time
        Space Complexity: O(1) list
        
        """
