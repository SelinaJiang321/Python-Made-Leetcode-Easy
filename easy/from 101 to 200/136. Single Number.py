"""

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

Follow up: Could you implement a solution with a linear runtime complexity and without using extra memory?

 

Example 1:

Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4
Example 3:

Input: nums = [1]
Output: 1
 

Constraints:

1 <= nums.length <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
Each element in the array appears twice except for one element which appears only once.

"""

# Hash Table Solution
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # create a new dictionary
        dic = {}
        # traverse the numbers in the list nums
        for num in nums:
            # .get() funciton -> to get the value of the key in python
            # get() function: key, default=None
            # since we need to set the default value of each number to 0 so we use get(num, 0)
            dic[num] = dic.get(num, 0) + 1
        # for dic.items() function:
        # we can fetch the key and value of each item in the dictionary
        for key, value in dic.items():
            if value == 1:
                return key

        # Any comments or advice?
        
