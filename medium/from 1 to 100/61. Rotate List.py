"""


Given the head of a linked list, rotate the list to the right by k places.

 

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
Example 2:


Input: head = [0,1,2], k = 4
Output: [2,0,1]
 

Constraints:

The number of nodes in the list is in the range [0, 500].
-100 <= Node.val <= 100
0 <= k <= 2 * 109


"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        
        if head is None: return None
        if head.next is None: return head
        
        # try to find the length of the linked list
        newHead = head
        length = 0
        while (newHead):
            newHead = newHead.next
            length += 1
            
        k = k % length
        # allocate a new node
        prev, curr = head, head
        
        # each time rotate the end to the head of the list
        for i in range(0,k):
            # the curr node is the tail of the linked list
            while curr.next:
                prev = curr
                curr = curr.next
            
            # to link the tail to the head
            prev.next = None
            curr.next = head
            head = curr
            # reassign the curr and prev node to the head
            curr , prev = head, head
            
        return head
      
      
