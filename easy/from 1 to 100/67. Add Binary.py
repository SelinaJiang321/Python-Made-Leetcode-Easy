"""
Given two binary strings a and b, return their sum as a binary string.

 

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
 

Constraints:

1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.

"""

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        
        i, j = len(a)-1, len(b)-1
        res = ""
        carry = 0
        
        # when we process calculation, we always need a carry
        
        while i >= 0 or j >= 0:
            a_digit = int(a[i]) if i >=0 else 0
            b_digit = int(b[j]) if j >=0 else 0
            sum_digits = a_digit + b_digit + carry
            # either 1 or 0
            carry = sum_digits // 2
            # either 1 or 0
            digit = sum_digits % 2
            # the sequence is important since we need to add the digit to the most sig bit
            res = str(digit) + res
            i -= 1
            j -= 1
            
        if (carry):
            # sequence is important here as well
            res = str(carry) + res
        
        return res
        
        # Time complexity: O(1) Space complexity: o(1)
