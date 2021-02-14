"""

Given an array of integers nums.

A pair (i,j) is called good if nums[i] == nums[j] and i < j.

Return the number of good pairs.

 

Example 1:

Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
Example 2:

Input: nums = [1,1,1,1]
Output: 6
Explanation: Each pair in the array are good.
Example 3:

Input: nums = [1,2,3]
Output: 0

"""

class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        Solution one: brute force
        
        res = 0 
        for i in range(len(nums)):
            for j in range(i + 1,len(nums)):
                if nums[i] == nums[j]:
                    res += 1
        
        return res
        
        # Time: O(n^2) Space: O(1)
       
        
        # a hash table (dictionary) with one for loop
        
        repeated = {}
        num = 0
        
        # for element in the number
        for value in nums:
            
            # if the value is in repeated dictionary
            if value in repeated:
                
                # count number of dulicates based on the values
                num += repeated[value]
                repeated[value] += 1
            else:
                repeated[value] = 1
                
        return num
        
        # Time:O(n) Space: O(1)
        
        # Any comments?
        
                    
