"""

Given a non-negative integer num, repeatedly add all its digits until the result has only one digit.

Example:

Input: 38
Output: 2 
Explanation: The process is like: 3 + 8 = 11, 1 + 1 = 2. 
             Since 2 has only one digit, return it.
Follow up:
Could you do it without any loop/recursion in O(1) runtime?

"""

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        
        # the theorem is that The original number is divisible by 9 if and only if the sum of its digits is divisible by 9
        
        if num == 0:
            return 0
        
        elif num % 9 == 0:
            return 9
        else:
            return num % 9
            
        # Can't think of a better algorithm:(
