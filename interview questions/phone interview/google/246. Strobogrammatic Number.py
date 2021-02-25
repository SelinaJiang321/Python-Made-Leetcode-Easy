"""

A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Write a function to determine if a number is strobogrammatic. The number is represented as a string.

 

Example 1:

Input: num = "69"
Output: true
Example 2:

Input: num = "88"
Output: true
Example 3:

Input: num = "962"
Output: false
Example 4:

Input: num = "1"
Output: true

"""

class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        digits = {'0': '0', '1': '1', '8': '8', '6': '9', '9': '6'}
        
        array = []
        
        # reversed the whole number to track is the main step
        # no need to cast the string into an integer
        # just add the character
        # and cast the list into a string and then compare two strings
        for char in reversed(num) :
            if char not in digits:
                return False
            array.append(digits[char])
            
            result = "".join(array)
            
        return result == num
      
      # Time :O(n)
      # Space: O(n)
