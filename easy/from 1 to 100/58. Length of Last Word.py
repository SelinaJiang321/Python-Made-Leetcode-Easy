"""

Given a string s consists of some words separated by spaces, return the length of the last word in the string. If the last word does not exist, return 0.

A word is a maximal substring consisting of non-space characters only.

 

Example 1:

Input: s = "Hello World"
Output: 5
Example 2:

Input: s = " "
Output: 0
 

Constraints:

1 <= s.length <= 104
s consists of only English letters and spaces ' '.


"""

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        # .split() funciton is to split the string into words 
        # for example, txt = "hello, my name is Peter, I am 26 years old"
        # x = txt.split(", ")
        # then it will be  ['hello', 'my name is Peter', 'I am 26 years old']
        # since here we just need to split according to the space
        # Attention: if there is a space after the word, it will return a wrong answer if we use s.split(" ")
        # for example ,like "a ", we will return 0 instead of one. so we need to use s.split()
        s = s.split()
        
        if s:
            # return the last word
            return len(s[-1])
        return 0
            
