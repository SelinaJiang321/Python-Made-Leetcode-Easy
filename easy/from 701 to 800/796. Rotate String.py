"""

We are given two strings, A and B.

A shift on A consists of taking string A and moving the leftmost character to the rightmost position. For example, if A = 'abcde', then it will be 'bcdea' after one shift on A. Return True if and only if A can become B after some number of shifts on A.

Example 1:
Input: A = 'abcde', B = 'cdeab'
Output: true

Example 2:
Input: A = 'abcde', B = 'abced'
Output: false
Note:

A and B will have length at most 100.

"""

class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B) : return False
        if len(A) == 0: return True
        
        res = A
        for character in A:
            res = res[1:] + character
            if res == B:
                return True
        
        return False
      
        # we need to clarify that the len(A) should take into account first. 
        # like if len(A) == 0 we need to return true
        
