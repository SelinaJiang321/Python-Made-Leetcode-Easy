"""

Given a fixed length array arr of integers, duplicate each occurrence of zero, shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written.

Do the above modifications to the input array in place, do not return anything from your function.

 

Example 1:

Input: [1,0,2,3,0,4,5,0]
Output: null
Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]
Example 2:

Input: [1,2,3]
Output: null
Explanation: After calling your function, the input array is modified to: [1,2,3]
 

Note:

1 <= arr.length <= 10000
0 <= arr[i] <= 9

"""


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
      
       """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        
        zeroes = arr.count(0)
        n = len(arr)
        for i in range(n-1, -1, -1):
            if i + zeroes < n:
                arr[i + zeroes] = arr[i]
            if arr[i] == 0: 
                zeroes -= 1
                if i + zeroes < n:
                    arr[i + zeroes] = 0
                    
       """
      original arr:
      [1, 0, 2, 0, 3, 0]
      num of zeros so far:
      [0, 1, 1, 2, 2, 3]
      arr with duplicate 0s (Θ means a duplicate 0):
      [1, Θ, 0, 2, Θ, 0, 3, Θ, 0]
      arr after cutoff
      [1, Θ, 0, 2, Θ, 0]

      # Every number in the original array is shifted to the right by the number of zeros so far.
      # Because of the cutoff, we are going to check if the new position of the number is inside the array.
      if i + zeroes < n:
      # This is checking if there is a Θ that should be included.
      if arr[i] == 0:
        zeroes -= 1
        if i + zeroes < n:
           arr[i + zeroes] = 0
       
       
       """
