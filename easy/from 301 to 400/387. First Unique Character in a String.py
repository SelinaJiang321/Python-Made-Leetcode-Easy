"""

Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode"
return 2.
 

Note: You may assume the string contains only lowercase English letters.

"""

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        #search elements in a list->always hash map
        
        # create a hash map here by using collections.Counter
        
        res = collections.Counter(s)
        
        # enumerate function is for two iterable values: items and counts
        for index, character in enumerate(res):
            if res[character] == 1:
                return index
        return -1
        
        # Any comments?
        
        
