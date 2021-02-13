"""

Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True
Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
Note:
The string will only contain lowercase characters a-z. The maximum length of the string is 50000.

"""

class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        l, r = 0, len(s) - 1
        
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                # from the left hand side and the right hand side we try to remove one element to see if that's possible
                tmp1 = s[:l] + s[l+1:]
                tmp2 = s[:r] + s[r+1:]
                
                # this is the only chance and then we can directly check
                return tmp1 == tmp1[::-1] or tmp2 == tmp2[::-1]
        # l == r
        return True
        
        # Any comments?
        
        
