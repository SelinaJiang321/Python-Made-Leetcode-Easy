"""


Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
Example 4:

Input: s = "([)]"
Output: false
Example 5:

Input: s = "{[]}"
Output: true
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        # create a dictionary with the corresponding brackets
        dic = {'{':'}', '[':']','(':')'}
        
        stack = []
        
        for item in s:
            # if item is '{''[''(' we append '}' ']' ')'
            if item in dic.keys():
                stack.append(dic[item])
            elif item in dic.values():
                try:
                    # if that ')' ']' '}' doesn't correspond to the brackets before
                    # we just return false
                
                    if item.values != stack.pop:
                        return False
                # exception is the code to handle the error
                exception:
                    return False
            # invalid input
            else:
                return False
        # finally the stack == 0 then it's true
        if len(stack) == 0:
                return True
                
        # Any comments or advice?
