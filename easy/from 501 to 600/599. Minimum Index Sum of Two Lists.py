"""

Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of favorite restaurants represented by strings.

You need to help them find out their common interest with the least list index sum. If there is a choice tie between answers, output all of them with no order requirement. You could assume there always exists an answer.

 

Example 1:

Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
Output: ["Shogun"]
Explanation: The only restaurant they both like is "Shogun".
Example 2:

Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["KFC","Shogun","Burger King"]
Output: ["Shogun"]
Explanation: The restaurant they both like and have the least index sum is "Shogun" with index sum 1 (0+1).
Example 3:

Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["KFC","Burger King","Tapioca Express","Shogun"]
Output: ["KFC","Burger King","Tapioca Express","Shogun"]
Example 4:

Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["KNN","KFC","Burger King","Tapioca Express","Shogun"]
Output: ["KFC","Burger King","Tapioca Express","Shogun"]
Example 5:

Input: list1 = ["KFC"], list2 = ["KFC"]
Output: ["KFC"]
 

Constraints:

1 <= list1.length, list2.length <= 1000
1 <= list1[i].length, list2[i].length <= 30
list1[i] and list2[i] consist of spaces ' ' and English letters.
All the stings of list1 are unique.
All the stings of list2 are unique.

"""

class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        leastIndex = len(list1)
        res = ""
        for index1, rest1 in enumerate(list1):
            for index2, rest2 in enumerate(list2):
                if rest1 == rest2:
                    index = index1 + index2
                    if index < leastIndex:
                        res = res.append(rest1)
                    elif index == leastIndex:
                        res = res + rest1
                    
        return res
    
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        words1 = {word: idx for idx, word in enumerate(list1)}

        min_sum = math.inf
        for idx2, word2 in enumerate(list2):
            if word2 in words1:
                if words1[word2] + idx2 < min_sum:
                    min_sum = words1[word2] + idx2
                    min_words = [word2]
                elif words1[word2] + idx2 == min_sum:
                    min_words.append(word2)
                   
        return min_words
        
        
