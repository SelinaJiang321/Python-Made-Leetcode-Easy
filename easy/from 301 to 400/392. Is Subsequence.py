"""
Given two strings s and t, check if s is a subsequence of t.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
 

Constraints:

0 <= s.length <= 100
0 <= t.length <= 104
s and t consist only of lowercase English letters.

"""

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        start = 0
        
        # just to check each character in the string
        for c in s:
            i = t.find(c,start)
            # the find funciton will return the index of that character
            # will return -1 if it couldn't be found
            if i == -1:
                return False
            # and will find the value from the next index
            start = i + 1
            
        return True
        
        # Time: O(1) Space: O(1)
        
        # Any comments?
        
