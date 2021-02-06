"""


Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
 

Constraints:

s consists only of printable ASCII characters.
"""

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # we need to judge whether it is a palindrome or not then we have to ignore other notations but to compare the characters
        # so we use a function named isalnum() to combine each character in a string by using "".join()
        # then we need to examine if they are all lower cases; if not then change them into lower case
        # at last, we compare s and s[::-1]
        # attention: this is an array slicing here, so [::-1] means from last element to the head , step is -1
        # while list[:-1] means from the second last element to the first element and the step is -1
        new_s = "".join([c for c in s if c.isalnum()])
        new_s = new_s.lower()
        return new_s == new_s[::-1]
       
        # all the palindromes can be solved like this
        # any advice or comment?
        
        
