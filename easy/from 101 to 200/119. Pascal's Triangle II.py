"""

Given an integer rowIndex, return the rowIndexth row of the Pascal's triangle.

Notice that the row index starts from 0.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Follow up:

Could you optimize your algorithm to use only O(k) extra space?

 

Example 1:

Input: rowIndex = 3
Output: [1,3,3,1]
Example 2:

Input: rowIndex = 0
Output: [1]
Example 3:

Input: rowIndex = 1
Output: [1,1]
 

Constraints:

0 <= rowIndex <= 33

"""

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        
        res = [[0 for _ in range(i+1)] for i in range(rowIndex + 1)]
        # Intialise each number as 0
        
        def helper(i,j):
            # put the right number into the right place
            if j == 0 or j == i: return 1
            if res[i][j] == 0:
                res[i][j] = res[i-1][j-1] + res[i-1][j]
            return res
            
        # create a new array to store the numbers    
        row = res[rowIndex]
        for j in range(rowIndex + 1):
            # to get the corresponding values
            row[j] = helper(rowIndex, j)
        # return the whole array 
        return row
        
        # we may use extra space here, no idea how to optimise it atm.
        # Any comments?
        
