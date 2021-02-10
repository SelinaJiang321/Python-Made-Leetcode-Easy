"""

Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
    ...
Example 1:

Input: 1
Output: "A"
Example 2:

Input: 28
Output: "AB"
Example 3:

Input: 701
Output: "ZY"

"""

class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        
        # chr is the function to turn a number into a character; ord() funciton is to turn a character into a number
        capitals = [chr(x) for x in range(ord('A'),ord('Z')+1)
        result = []
        
        while n > 0:
            # we can append the character, since we only have 0-25
            result.append(capitals[(n-1) % 26])
            
            n = (n - 1) // 26
            
        # reverse the string
        result.reverse()
        # join together all the characters
        result = ''.join(result)
        
        return result
        
        # Any comments?
        
        
