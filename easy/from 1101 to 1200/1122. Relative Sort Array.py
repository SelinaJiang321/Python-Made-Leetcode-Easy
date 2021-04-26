"""
Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.

Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2.  Elements that don't appear in arr2 should be placed at the end of arr1 in ascending order.

 

Example 1:

Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
Output: [2,2,2,1,4,3,3,9,6,7,19]
 

Constraints:

1 <= arr1.length, arr2.length <= 1000
0 <= arr1[i], arr2[i] <= 1000
All the elements of arr2 are distinct.
Each arr2[i] is in arr1.


"""

class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        
        c = {}
        list1 = []             #common elements
        list2 = []             #leftover elements
        for n in arr1:
            if n in c:
                c[n]+=1
            else:
                c[n]=1
        for n in arr2:
            while c[n]:
                list1.append(n)
                c[n]-=1
            del c[n]
        for n in sorted(c.keys()):
            while c[n]:
                list2.append(n)
                c[n]-=1
        return list1+list2
