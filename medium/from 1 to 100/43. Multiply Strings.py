"""
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

 

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
 

Constraints:

1 <= num1.length, num2.length <= 200
num1 and num2 consist of digits only.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.



"""

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        
        s1, s2 = num1[::-1], num2[::-1]
        
        ans = 0
        tens_s1 = 1
        for digit1 in s1:
            tens_s2 = 1
            for digit2 in s2:
                ans += tens_s1 * (ord(digit1) - ord('0')) * tens_s2 * (ord(digit2) - ord('0'))
                tens_s2 *= 10
            tens_s1 *= 10
        return str(ans)
