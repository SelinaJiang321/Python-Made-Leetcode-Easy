"""
Given a string paragraph and a string array of the banned words banned, return the most frequent word that is not banned. It is guaranteed there is at least one word that is not banned, and that the answer is unique.

The words in paragraph are case-insensitive and the answer should be returned in lowercase.

 

Example 1:

Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
Output: "ball"
Explanation: 
"hit" occurs 3 times, but it is a banned word.
"ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph. 
Note that words in the paragraph are not case sensitive,
that punctuation is ignored (even if adjacent to words, such as "ball,"), 
and that "hit" isn't the answer even though it occurs more because it is banned.
Example 2:

Input: paragraph = "a.", banned = []
Output: "a"
 

Constraints:

1 <= paragraph.length <= 1000
paragraph consists of English letters, space ' ', or one of the symbols: "!?',;.".
0 <= banned.length <= 100
1 <= banned[i].length <= 10
banned[i] consists of only lowercase English letters.

"""

class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        
        new_para = ""
        ste = "!?',;.':"
        for i in paragraph:
            if i in ste:
                new_para += ' '
                continue       
            new_para += i
        text = new_para.split(' ')
        for i in range(len(text)):
            text[i] = text[i].lower()
        data = collections.Counter(text)
        max_val = 0
        max_char = ''
        print(data)
        for key,val in data.items():
            if key in banned or key == "":
                continue
            else:
                if max_val < val:
                    max_char = key
                    max_val = val
        return max_char
      
        # take-away: collections.Counter() is a dictionary which counts the character and the times that the character shows up
        # .items() show the whole dictionary with key and values separately
