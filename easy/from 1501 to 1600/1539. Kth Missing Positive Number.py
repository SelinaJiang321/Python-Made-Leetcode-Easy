"""

Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

Find the kth positive integer that is missing from this array.

 

Example 1:

Input: arr = [2,3,4,7,11], k = 5
Output: 9
Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.
Example 2:

Input: arr = [1,2,3,4], k = 2
Output: 6
Explanation: The missing positive integers are [5,6,7,...]. The 2nd missing positive integer is 6.
 

Constraints:

1 <= arr.length <= 1000
1 <= arr[i] <= 1000
1 <= k <= 1000
arr[i] < arr[j] for 1 <= i < j <= arr.length


"""

class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        
        # we divide this problem into two parts: one part is the number in the array

        results = [i for i in range(1, max(arr) + 1)]
        # we can sort the number by using set
        numSet = set(arr)
        
        count = 0
        for num in results:
            if num not in numSet:
                count += 1
                if count == k:
                    return num 
                  
        # if the kth number is outside of this array
        
        while count < k:
            count += 1
            num += 1
        return num
            
