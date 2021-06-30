"""

There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1
 

Constraints:

1 <= nums.length <= 5000
-104 <= nums[i] <= 104
All values of nums are unique.
nums is guaranteed to be rotated at some pivot.
-104 <= target <= 104

"""

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # find the index of pivot point first
        # divide the array into two sub-arrays
        # search the element in two sub-arrays separately
        
        
        # 3, 4, 5, 6, 1, 2  it returns 3
        
        def pivot(arr,lo,hi):
            if (hi < lo) :
                return -1
            
            if (hi == lo):
                return lo
            
            mid = (int)((lo + hi) / 2)
            
            
            # ensure not over the range of high and low
            if mid < hi and arr[mid + 1] < arr[mid]:
                return mid
            if mid > lo and arr[mid] < arr[mid-1]:
                return mid-1
            if arr[lo] >= arr[mid]:
                return pivot(arr,lo,mid-1)
            
            return pivot(arr,mid+1, hi)

        
        # binary search
        def binarysearch(arr,lo,hi,tar):
            if hi < lo: return -1
            mid = (int) ((hi + lo) / 2)
            
            if tar == arr[mid]: return mid
            if tar > arr[mid]: return binarysearch(arr,mid+1,hi,tar)
            
            return binarysearch(arr,lo,mid-1,tar)
        
        #main function
        n = len(nums)
        point = pivot(nums,0,n-1)
        
        
        if (point == -1) : return binarysearch(nums,0,n-1,target)
        
        else:
            #compare with the pivot first
            if (nums[point] == target): return point
            # search in the larger array
            if (target >= nums[0]): return binarysearch(nums,0,point-1,target)
            else: return binarysearch(nums, point +1 ,n-1,target)
        
