"""

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

0 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.

"""

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        # turn the string(iterable items) into the tuples
        # for example,strs = ["flower","flow","flight"]
        # l = list(zip(*strs))
        #  >>> l = [('f', 'f', 'f'), ('l', 'l', 'l'), ('o', 'o', 'i'), ('w', 'w', 'g')]
        l = list(zip(*str))
        
        # define an empty prefix
        prefix = ""
        for i in l:
            """
            Python sees a string as an ordered collection of characters. 
            'abc', is a collection of 'a', 'b', and 'c'. So every digit is seen as an element and added to the set.

            But adding the same digit a second time, has no effect. 
            So that means that we end up with a set where every digit is added once. 
            By then calculating the len(..) we obtain the number of unique digits. We can then compare that number with a given number.
            """
            # so if the len(set(i)) == 1 means there is only 1 unique character in that tuple
            if len(set(i)) == 1:
                # so the all three characters are the same and we just need to add the first one of the tuple
                prefix += i[0]
            else:
                break
        # return the string of the prefix
        return prefix
        
        # Any comments and advice
