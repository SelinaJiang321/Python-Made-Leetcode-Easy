"""

Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

 

Example 1:

Input: pattern = "abba", s = "dog cat cat dog"
Output: true
Example 2:

Input: pattern = "abba", s = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false
Example 4:

Input: pattern = "abba", s = "dog dog dog dog"
Output: false
 

Constraints:

1 <= pattern.length <= 300
pattern contains only lower-case English letters.
1 <= s.length <= 3000
s contains only lower-case English letters and spaces ' '.
s does not contain any leading or trailing spaces.
All the words in s are separated by a single space.

"""

class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        
        # create two dictionaries
        map_char = {}
        map_word = {}
        
        # the string and then what is the symbol to split
        words = s.split(' ')
        
        # to compare the lengths first
        if len(words) != len(pattern):
            return False
        
        # iterate between pattern and words
        for c, w in zip(pattern, words):
            # to check if the char in the dictionary or not
            if c not in map_char:
                # not one-to-one
                if w in map_word:
                    return False
                # to relate them together
                else:
                    map_char[c] = w
                    map_char[w] = c
            # need to check map_char instead of map_word since there may be words that don't appear before
            # For example, abba but fish dog dog cat, then there will be runtime error
            # wrong: map_word[w] != c
            
            else:
                if map_char[c] != w:
                    return False
        
        return True
        
        # Any comments?
        
