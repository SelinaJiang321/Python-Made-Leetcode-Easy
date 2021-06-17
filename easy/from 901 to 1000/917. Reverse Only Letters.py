"""
Given a string s, return the "reversed" string where all characters that are not a letter stay in the same place, and all letters reverse their positions.

 

Example 1:

Input: s = "ab-cd"
Output: "dc-ba"
Example 2:

Input: s = "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"
Example 3:

Input: s = "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"
 

Note:

s.length <= 100
33 <= s[i].ASCIIcode <= 122 
s doesn't contain \ or "

"""

class Solution(object):
    def reverseOnlyLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        # convert the string to a list of characters
        words = list(s)
        # store the reversed of the characters
        res_one = list(reversed(words))
        res = []
        # loop through the two list of characters
        # 
        count  = 0;
        for value in words :
            if value.isalpha() :
                while not res_one[count].isalpha():
                    count += 1
                        
                res.append(res_one[count])
                count += 1
            
            else:
                res.append(value)
              
        res = "".join(res)
        return res
        
