"""

Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4 
  / \
 1   2
Return true, because t has the same structure and node values with a subtree of s.
 

Example 2:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
    /
   0
Given tree t:
   4
  / \
 1   2
Return false.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if s is None: return False
        if s.val == t.val and self.isSame(s, t): return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
    
    def isSame(self, s, t):
        if s is None and t is None: return True
        if s is None or t is None: return False
        if s.val != t.val: return False
        
        return self.isSame(s.left, t.left) and self.isSame(s.right, t.right)
      
        # Time Complexity: O(m+n)
        # Space Complexity: O(1)
