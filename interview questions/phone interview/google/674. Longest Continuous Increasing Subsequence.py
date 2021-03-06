"""

Given an unsorted array of integers nums, return the length of the longest continuous increasing subsequence (i.e. subarray). The subsequence must be strictly increasing.

A continuous increasing subsequence is defined by two indices l and r (l < r) such that it is [nums[l], nums[l + 1], ..., nums[r - 1], nums[r]] and for each l <= i < r, nums[i] < nums[i + 1].

 

Example 1:

Input: nums = [1,3,5,4,7]
Output: 3
Explanation: The longest continuous increasing subsequence is [1,3,5] with length 3.
Even though [1,3,5,7] is an increasing subsequence, it is not continuous as elements 5 and 7 are separated by element
4.
Example 2:

Input: nums = [2,2,2,2,2]
Output: 1
Explanation: The longest continuous increasing subsequence is [2] with length 1. Note that it must be strictly
increasing.
 

Constraints:

0 <= nums.length <= 104
-109 <= nums[i] <= 109



"""

class Solution(object):
    def findLengthOfLCIS(self, nums):
        ans = anchor = 0
        for i in range(len(nums)):
            if i and nums[i-1] >= nums[i]: anchor = i
            ans = max(ans, i - anchor + 1)
        return ans
      
"""
Intuition and Algorithm

Every (continuous) increasing subsequence is disjoint, and the boundary of each such subsequence occurs whenever nums[i-1] >= nums[i]. When it does, it marks the start of a new increasing subsequence at nums[i], and we store such i in the variable anchor.

For example, if nums = [7, 8, 9, 1, 2, 3], then anchor starts at 0 (nums[anchor] = 7) and gets set again to anchor = 3 (nums[anchor] = 1). Regardless of the value of anchor, we record a candidate answer of i - anchor + 1, the length of the subarray nums[anchor], nums[anchor+1], ..., nums[i]; and our answer gets updated appropriately.

Time Complexity: O(N)O(N), where NN is the length of nums. We perform one loop through nums.

Space Complexity: O(1)O(1), the space used by anchor and ans

"""
