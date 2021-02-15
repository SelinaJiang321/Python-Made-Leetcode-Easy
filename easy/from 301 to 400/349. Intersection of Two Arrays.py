"""
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Note:

Each element in the result must be unique.
The result can be in any order.

"""

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        res = []
        
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    res.append(nums1[i])
                    
        return set(res) # to delete the repetitive elements
        
        # a better solution
        
class Solution(object):
def intersection(self, nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """
    res = []
    # to create a hash table and dictionary to store the times
    map = {}
    for i in nums1:
        map[i] = map[i]+1 if i in map else 1
    for j in nums2:
        # we need to check if j in map or not
        # if it is not in map, we can't check if map[j] is > 0 or not-> there will be an infinite loop then
        # a runtime error will appear
        
        if j in map and map[j] > 0:
            res.append(j)
            map[j] = 0
    
    return res

    # Is there any possibility that we can only use one hash table/one extra array to record this?

    # Any comments?
    
    
    
        
