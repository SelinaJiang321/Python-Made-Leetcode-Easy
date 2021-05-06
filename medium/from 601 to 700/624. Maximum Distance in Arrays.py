"""

You are given m arrays, where each array is sorted in ascending order.

You can pick up two integers from two different arrays (each array picks one) and calculate the distance. We define the distance between two integers a and b to be their absolute difference |a - b|.

Return the maximum distance.

 

Example 1:

Input: arrays = [[1,2,3],[4,5],[1,2,3]]
Output: 4
Explanation: One way to reach the maximum distance 4 is to pick 1 in the first or third array and pick 5 in the second array.
Example 2:

Input: arrays = [[1],[1]]
Output: 0
Example 3:

Input: arrays = [[1],[2]]
Output: 1
Example 4:

Input: arrays = [[1,4],[0,5]]
Output: 4
 

Constraints:

m == arrays.length
2 <= m <= 105
1 <= arrays[i].length <= 500
-104 <= arrays[i][j] <= 104
arrays[i] is sorted in ascending order.
There will be at most 105 integers in all the arrays.
"""

class Solution(object):
    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        """
        mn, mx = arrays[0][0], arrays[0][-1]
        diff = -float("inf")
        for ar in arrays[1:]:
            mx_diff = abs(mx - ar[0])
            mn_diff = abs(mn - ar[-1])
            diff = max(diff, mn_diff, mx_diff)
            if ar[0] < mn:
                mn = ar[0]
            if ar[-1] > mx:
                mx = ar[-1]
        return diff
        
        
