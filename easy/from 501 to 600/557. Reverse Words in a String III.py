"""
Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

 

Example 1:

Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Example 2:

Input: s = "God Ding"
Output: "doG gniD"
 

Constraints:

1 <= s.length <= 5 * 104
s contains printable ASCII characters.
s does not contain any leading or trailing spaces.
There is at least one word in s.
All the words in s are separated by a single space.
"""

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
          # O(n)
        # split the string
        split_s = s.split(" ")
        # instantiate result string
        result = ""
        # loop through list  
        for i in split_s:
            # reverse the element in list, our string
            result += i[::-1]
            # insert space
            result += " "
            # return everything other than the last element in string, which is just a extra space
        return result[:-1]
        
        #Take away:
        # return result[:-1] not result since by using index slicing we can avoid trailing space
        
