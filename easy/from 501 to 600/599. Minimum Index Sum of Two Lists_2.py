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

        # get lengths of each list
        length_list1 = len(list1)
        length_list2 = len(list2)
        
        # initialize list index sum as max of lengths
        list_index_sum = length_list1+length_list2
        
        # initialize empty list for common items
        common_items = []
        
        # loop over items in list 1
        index_1 = -1
        for item in list1:
            
            # computes list index for item in first list
            index_1 += 1
            
            # check if this item is in list 2
            if item in list2:
                
                # get list index for item in second list
                index_2 = list2.index(item)
                
                temp_index_sum = index_1+index_2
                
                # see if this index sum is less than or equal to previously lowest
                if temp_index_sum <= list_index_sum:
                    
                    # if they are equal, append item to list
                    if temp_index_sum == list_index_sum:
                        common_items.append(item)
                    
                    # if it is less, define new common items list
                    else:
                        common_items = [item]
                        
                    # set new list index sum
                    list_index_sum = temp_index_sum
        
        return common_items
      
      
