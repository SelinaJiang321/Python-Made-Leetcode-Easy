"""

Given an array of integers arr, write a function that returns true if and only if the number of occurrences of each value in the array is unique.

 

Example 1:

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
Example 2:

Input: arr = [1,2]
Output: false
Example 3:

Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true
 

Constraints:

1 <= arr.length <= 1000
-1000 <= arr[i] <= 1000
"""

class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        dic = {}
        for number in arr:
            if number in dic:
                dic[number] += 1
            else:
                dic[number] = 1
                
        # check unique values:
                
        
        hash_val = dict()
        for keys in dic:
            if dic[keys] in hash_val:
                return False
            else:
                hash_val[dic[keys]] = 1
                
        return True
        
        
        # Use of Hash Map
        # Dictionary
        
