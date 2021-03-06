"""
Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

 

Example 1:

Input: arr = [2,1]
Output: false
Example 2:

Input: arr = [3,5,5]
Output: false
Example 3:

Input: arr = [0,3,2,1]
Output: true
 

Constraints:

1 <= arr.length <= 104
0 <= arr[i] <= 104


"""


class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        flag = 0
        
        for i in range(len(arr) - 1):
            if (flag == 0):
                if arr[i] < arr[i+1]:
                    flag = 1
                else:
                    return False
            elif flag == 1:
                if arr[i] > arr[i+1]:
                    flag = 2
                elif arr[i] == arr[i+1]:
                    return False
                    
                
            else:
                if arr[i] <= arr[i+1] :
                    return False
        
        if flag == 0 or flag == 1:
            return False
        else:
            return True
        
"""
Complexity Analysis

Time Complexity: O(N)O(N), where NN is the length of A.

Space Complexity: O(1)O(1).
"""
        
class Solution(object):
    def validMountainArray(self, A):
        N = len(A)
        i = 0

        # walk up
        while i+1 < N and A[i] < A[i+1]:
            i += 1

        # peak can't be first or last
        if i == 0 or i == N-1:
            return False

        # walk down
        while i+1 < N and A[i] > A[i+1]:
            i += 1

        return i == N-1
'''      
Complexity Analysis

Time Complexity: O(N)O(N), where NN is the length of A.

Space Complexity: O(1)O(1).
