"""

Given a non-empty, singly linked list with head node head, return a middle node of linked list.

If there are two middle nodes, return the second middle node.

 

Example 1:

Input: [1,2,3,4,5]
Output: Node 3 from this list (Serialization: [3,4,5])
The returned node has value 3.  (The judge's serialization of this node is [3,4,5]).
Note that we returned a ListNode object ans, such that:
ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next = NULL.
Example 2:

Input: [1,2,3,4,5,6]
Output: Node 4 from this list (Serialization: [4,5,6])
Since the list has two middle nodes with values 3 and 4, we return the second one.
 

Note:

The number of nodes in the given list will be between 1 and 100.

"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy_node = head
        length = 0
        while dummy_node is not None:
            dummy_node = dummy_node.next
            length += 1
        #print(length)
        

        index = (length // 2 ) + 1

        dummy_node_1 = head
        #print(index)
        iterate = 1
        while iterate < index:
            dummy_node_1 = dummy_node_1.next
            iterate += 1
            
        return dummy_node_1
     
#Fast and Slow pointer is always the case
        """
        Intuition and Algorithm

When traversing the list with a pointer slow, make another pointer fast that traverses twice as fast. 
When fast reaches the end of the list, slow must be in the middle.
        
        """
        
class Solution:
    def middleNode(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
        
        """
        
        Complexity Analysis

        Time Complexity: O(N)O(N), where NN is the number of nodes in the given list.

        Space Complexity: O(1)O(1), the space used by slow and fast.
        
        """
