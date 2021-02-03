"""
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.
Example 1:
Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:
Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:
Input: nums = [1,2,3,1,2,3], k = 2
Output: false
"""

""""
For questions like this, we want to keep track of the indices of the elements as well as the value.Thus, using dictionary for the list conversion is the most efficient way.
"""


def containsNearbyDuplicate(self, nums, k):
    # to create an empty dictionary
    dic = {}
    # enumerate function adds counter to an iterable and returns it
    # i stands for the counter, v stands for the value(item) inside
    # we are keeping track of two variables: i and v
    # for example, there is a list nums[1,2,3,1]
    # i = 0 , v is not in dic, dic[1] = 0
    # i = 1 , v is not in dic, dic[2] = 1
    # i = 2 , v is not in dic, dic[3] = 2
    # i = 3 , v == 1 is in dic, 3 - dic[1]  = 0 <= k?
    # yes, return True; else: return False
    for i, v in enumerate(nums):
        if v in dic and i - dic[v] <= k:
            return True
        dic[v] = i
    return False

    # Any comments and advice?
