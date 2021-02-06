"""
Given a non-negative integer x, compute and return the square root of x.

Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.

 

Example 1:

Input: x = 4
Output: 2
Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.
 

Constraints:

0 <= x <= 231 - 1

"""

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        # to search for the middle value
        l, r = 0 , x
        
        
        while l <= r:
            # value of mid is always the (left end + right end) /2
            mid = (r + l) // 2
            
            # for example, x = 9, mid = 4, 4*4 > 16, right end = mid - 1
            # else, like x = 5, mid = 2, 4 < 5 <= 9, return 5
            # else, like x = 10, mid = 5, 25> 10 ,right = 4; mid = 2, 10 > 9, then l = mid + 1 = 3; mid = (3 + 4)/2 = 3, satisfies the condition, returns 3
            if mid * mid <= x < (mid+1) * (mid + 1):
                return mid
            elif mid * mid > x:
                r  = mid - 1
            else:
                l = mid + 1
        
