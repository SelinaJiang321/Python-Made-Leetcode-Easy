"""

Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Example 1:

Input: [1,2,3,1]
Output: true
Example 2:

Input: [1,2,3,4]
Output: false
Example 3:

Input: [1,1,1,3,3,4,3,2,4,2]
Output: true

"""


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # list.sort() and sorted(list) differences:
        # list.sort(key=..., reverse=...)  sorted(list, key=..., reverse=...)
        
        """
        Sort in Descending order
        The sort() method accepts a reverse parameter as an optional argument.

        Setting reverse = True sorts the list in the descending order.

        list.sort(reverse=True)
        Alternately for sorted(), you can use the following code.

        sorted(list, reverse=True)
        
        Note: A list also has the sort() method which performs the same way as sorted(). 
        The only difference is that the sort() method doesn't return any value and changes the original list.


        
        """
        n = sorted(nums)
        for i in range(0,len(nums)-1, 1):
            if nums[i] == nums[i+1]:
                return True
        return False
