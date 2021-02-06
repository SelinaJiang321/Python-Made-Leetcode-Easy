"""


Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 

Constraints:

n == nums.length
1 <= n <= 5 * 104
-231 <= nums[i] <= 231 - 1

"""

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # the description of the problem is that the majority element appears more than [n/2] times 
        # so we can sort the elements in ascending or descending order, and then we can return the middle elements which must be the majority element
        # list.sort() to sort out the list in a certain order
        nums.sort()
        return nums[len(nums) // 2]
       
        # time complexity: O(nlgn) sorting the arrays in python is nlogn time, which is the domain funciton
        # space complexity: O(1) sort the array, linear space
