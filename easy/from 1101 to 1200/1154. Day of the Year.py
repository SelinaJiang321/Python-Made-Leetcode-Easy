"""

Given a string date representing a Gregorian calendar date formatted as YYYY-MM-DD, return the day number of the year.

 

Example 1:

Input: date = "2019-01-09"
Output: 9
Explanation: Given date is the 9th day of the year in 2019.
Example 2:

Input: date = "2019-02-10"
Output: 41
Example 3:

Input: date = "2003-03-01"
Output: 60
Example 4:

Input: date = "2004-03-01"
Output: 61
 

Constraints:

date.length == 10
date[4] == date[7] == '-', and all other date[i]'s are digits
date represents a calendar date between Jan 1st, 1900 and Dec 31, 2019.

"""

class Solution(object):
    def is_leap(self, year):
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
    def dayOfYear(self, date):
        """
        :type date: str
        :rtype: int
        """
        year, month, day = map(int, date.split('-'))
        months_to_days = [None, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        months_to_days[2] += self.is_leap(year)
        day_of_year = sum(months_to_days[i] for i in range(1, month)) + day
        return day_of_year
      
      # Take away: 1. Processing Multiple Input Iterables 2. With Different Kinds of Functions 3.Transforming Iterables of Strings
