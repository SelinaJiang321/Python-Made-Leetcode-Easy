"""

Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?

"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        rev = None
        fast = slow = head
        
        # since the fast is one time faster than slow, so when fast.next == None, slow must be in the middle
        while fast and fast.next:
            fast = fast.next.next
            # try to construct a reversed half linked lisy here
            rev, slow, rev.next = slow, slow.next, rev
            
        if fast:
            # construct another half linked list
            slow = slow.next
            
        while rev and rev.val == slow.val:
            rev = rev.next
            slow = slow.next
        
        # if rev == None, then not rev returns true; else return false( rev.vel != slow.val)
        return not rev
        
        # Any comment?
        
