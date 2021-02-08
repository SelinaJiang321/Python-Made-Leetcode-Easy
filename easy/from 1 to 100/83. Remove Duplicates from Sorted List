"""
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.
Example 1:


Input: head = [1,1,2]
Output: [1,2]
Example 2:


Input: head = [1,1,2,3,3]
Output: [1,2,3]
 

Constraints:

The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.

"""


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        
        if len(nums) == 0: return 0
        i = 0
        
        for j in range(1, len(nums)):
            # there is a different element 
            if nums[j] != nums[i]:
                # then we can increment the i and then assign the value to nums[i]
                i += 1
                nums[i] = nums[j]
        # since for the index we start from 0 so for the length we add one
        return i + 1
        
