"""

Given a year Y and a month M, return how many days there are in that month.

 

Example 1:

Input: Y = 1992, M = 7
Output: 31
Example 2:

Input: Y = 2000, M = 2
Output: 29
Example 3:

Input: Y = 1900, M = 2
Output: 28
 

Note:

1583 <= Y <= 2100
1 <= M <= 12

"""
class Solution(object):
    def numberOfDays(self, Y, M):
        """
        :type Y: int
        :type M: int
        :rtype: int
        """
        # different map for leap/non_leap years
        d_no_leap = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
        d_leap = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31} 
        # key: check if the given Y is a leap year
        if Y%4 == 0 and Y%100 != 0:
            # yes
            return(d_leap[M])
        elif Y%400 == 0:
            # yes
            return(d_leap[M])
        else:
            # no
            return(d_no_leap[M])
          
