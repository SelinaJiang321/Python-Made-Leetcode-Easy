"""
Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.

 

Example 1:


Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: l1 = [], l2 = []
Output: []
Example 3:

Input: l1 = [], l2 = [0]
Output: [0]
 

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both l1 and l2 are sorted in non-decreasing order.

"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        # if the head of l1 or l2 is none then we can just return a linked list
        if None in (l1, l2):
            return l1 or l2
            
        # quite common to set a dummy head just to check the head case
        dummy = curr = ListNode(0)
        dummy.next = l1
        
        while l1 and l2:
            # then it's sorted
            if l1.val < l2.val:
                l1 = l1.next
            else:
                # store the value of curr.next which is l1.next
                nxt = curr.next
                curr.next = l2
                tmp = l2.next
                l2.next = nxt
                l2 = tmp
            curr = curr.next
        
        curr.next = l1 or l2
        return dummy.next
                
        
