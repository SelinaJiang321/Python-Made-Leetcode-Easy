"""

Given an integer, write an algorithm to convert it to hexadecimal. For negative integer, two’s complement method is used.

Note:

All letters in hexadecimal (a-f) must be in lowercase.
The hexadecimal string must not contain extra leading 0s. If the number is zero, it is represented by a single zero character '0'; otherwise, the first character in the hexadecimal string will not be the zero character.
The given number is guaranteed to fit within the range of a 32-bit signed integer.
You must not use any method provided by the library which converts/formats the number to hex directly.
Example 1:

Input:
26

Output:
"1a"
Example 2:

Input:
-1

Output:
"ffffffff"

"""

class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        
        if num == 0: return 0
        
        mp = "123456789abcdef"
        rs = ""
        
        for i in range(8):
            # need to add them at the end of the string
            rs = mp[num % 16] + rs
            # to divide it to get the more sig bit
            # bit operation is slower so don't use num = num >> 4
            num = num // 16
         
         # to remove the zeros of the beginning of the string
         return rs.lstrip('0')
         
         # O(n) O(1)
         
         # Any comments?
         
