"""
Given the array of integers nums, you will choose two different indices i and j of that array. Return the maximum value of (nums[i]-1)*(nums[j]-1).
 

Example 1:

Input: nums = [3,4,5,2]
Output: 12 
Explanation: If you choose the indices i=1 and j=2 (indexed from 0), you will get the maximum value, that is, (nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 = 12. 
Example 2:

Input: nums = [1,5,4,5]
Output: 16
Explanation: Choosing the indices i=1 and j=3 (indexed from 0), you will get the maximum value of (5-1)*(5-1) = 16.
Example 3:

Input: nums = [3,7]
Output: 12
 

Constraints:

2 <= nums.length <= 500
1 <= nums[i] <= 10^3

"""

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        product = 0
        
        for i in range(len(nums)):
            for j in range(len(nums)):
                if ((nums[i] - 1) * (nums[j] - 1) >= product) and  i != j :
                    product = (nums[i] - 1) * (nums[j] - 1)
                    print(i,j)
                    
                    
        return product
        
       # time complexity is O(n^2)
       # A better way is to use linear scan
        
class Solution(object):
    def maxProduct(self, nums):

        first, second = 0, 0
        
        for number in nums:
            
            if number > first:
                # update first largest and second largest
                first, second = number, first
                
            else:
                # update second largest
                second = max( number, second)
        
        return (first - 1) * (second - 1)
      
      # by keep updating the first and second to get the first and second largest numbers
      # so that we can use only one loop:O(n)
