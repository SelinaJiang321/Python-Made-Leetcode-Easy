"""
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.

"""

class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        # an array of strings
        result, nums = 0, [nums1, nums2]
        
        for num in nums:
            for index, item in enumerate(num[::-1]):
                # you need to use int() function to transform the string to an int
                result += (10** index * int(item))
        
        # need to transform the int result to the string
        return str(result)
        
        # O(n^2)-> nested for loop
        # O(n) extra space and array
            
