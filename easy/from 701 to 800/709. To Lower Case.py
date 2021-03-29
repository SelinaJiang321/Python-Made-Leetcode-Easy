"""

Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.

 

Example 1:

Input: "Hello"
Output: "hello"
Example 2:

Input: "here"
Output: "here"
Example 3:

Input: "LOVELY"
Output: "lovely"
"""

class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        #built-in funtion
        #return str.lower()
        
        
        #take away: one list comprehension here so if do something else then just append the char in the str
        #by getting the ascii value, you need to use ord to compare the value
        return ''.join([chr(ord(char)+32) if 65 <= ord(char) <= 90 else char for char in str])
