"""

Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]


"""

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        
        array = []
        
        for i in range(1, numRows + 1):
            temp = [1] * i
            array.append(array)
            
        for rows in range(len(array)):
        # we calculate until len(array) -1
            # all are one
            if row == 0 or row == 1:
                continue
            for column in range(len(array)-1):
            # we can only reach len(array) -2 since the last one is always one
                if column == 0:
                    array[row][column] = 1
                else:
                    array[row][column] = array[row-1][column-1] + array[row-1][column]
          
         return array
         
         
         # Time: O(n^2) Space: O(n)
         
         # Any comments?
             
