"""

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2
Example 3:

Input: root = []
Output: 0
Example 4:

Input: root = [0]
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100


"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #recursive function and BFS
        
         if not root: 
            return 0
    
        return max(self.maxDepth(root.left),self.maxDepth(root.right)) + 1
        
        """
        Explanation:
        
        Suppose: root=[10,null, 3,2,null]
        
        1. max(self.maxDepth(None),self.maxDepth(3)) + 1
        2. max(0,max(self.maxDepth(2),self.maxDepth(null))+1)
        3. max(0,max(max(self.maxDepth(null),self.maxDepth(null)+1),+ 1)+1)
        4. max(0,max(max(0,1)+ 1)+1)
        5. max(0,2)+1
        6. 2 + 1
        7. 3
        
        # Any comments?
        

        """
