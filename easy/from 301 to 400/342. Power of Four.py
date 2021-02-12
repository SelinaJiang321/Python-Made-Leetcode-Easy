"""

Given an integer n, return true if it is a power of four. Otherwise, return false.

An integer n is a power of four, if there exists an integer x such that n == 4x.

 

Example 1:

Input: n = 16
Output: true
Example 2:

Input: n = 5
Output: false
Example 3:

Input: n = 1
Output: true
 

Constraints:

-231 <= n <= 231 - 1


"""

class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        # rememebr to ask about the corner case like ZERO AND MIN_NUM AND MAX_NUM
        if n == 0:
            return False
        
        while n % 4 == 0:
            n /= 4
            
        return n == 1
        
       # Any comments?
       
       
        
