"""

Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?


"""

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # hash table to store the keys as well as the values
        # create a dictionary
        counter = {}
        
        if (len(s) != len(t)) : return False
        
        for char in s:
            if char not in counter:
                counter[char] = 1
            else:
                counter[char] += 1
                
       for char in t:
           if char in counter:
               counter[char] -= 1
           else: return False
           
       # .values() is a function to return the values of a dictionary  
       for val in counter.values():
            if val != 0: return False
       return True
        
       # Any comments?
       
       
        
