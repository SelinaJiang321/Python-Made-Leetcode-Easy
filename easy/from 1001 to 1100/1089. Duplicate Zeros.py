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

class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        items = len(arr)
        item = 0
        flag = False
        
        while item < items:
            if arr[item] == 0:
                arr.insert(item + 1, 0)
                del arr[-1] 
                flag = True
            if flag:
                item += 1
                flag = False
            item += 1
            
       # Time complexity: O(n)
       # Take away: we can delete the last element in the array by using del arry[-1]
       # Another way is by using remove function
      
