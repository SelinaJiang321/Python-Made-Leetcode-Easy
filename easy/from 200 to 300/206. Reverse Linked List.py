"""

Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        node = head
        
        while node:
            curr = node.next
            # Attention: don't write curr.next = node. then there will be a loop here and the curr can't move forward
            # the logic here is move curr first, and then let node.next = prev
            # then move prev and curr forward
            # until node = None, return prev: the last valid node
            node.next = prev
            prev = node
            node = curr
       return prev
        
