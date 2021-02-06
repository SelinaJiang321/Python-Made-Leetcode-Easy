"""
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:

Input: "hello"
Output: "holle"
Example 2:

Input: "leetcode"
Output: "leotcede"
Note:
The vowels does not include the letter "y".

"""

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        # transform the string to a list of vowels
        s = list(s)
        # to create a set of vowels that can be used to compare
        vows = set('aeiouAEIOU')
        
        l, r = 0, len(s) - 1
        
        
        while l <= r:
            # loop until there are vowels
            while l <= r and s[l] not in vows: l += 1
            while l <= r and s[r] not in vows: r -= 1
            if l > r: break
            # if there are vowels in place, just exchange their elements
            s[l], s[r] = s[r], s[l]
            l, r = l+1, r-1
        
        # join the list as a string, same as "".join(s) here
        # if you use ',' , then "hello" becomes "h,o,l,l,e"
        return ''.join(s)
            
        # Any advice or comments?
