"""
Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1

Trivia:
This problem was inspired by this original tweet by Max Howell:

Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so f*** off.

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree1(self, root):
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                node.left,node.right = node.right, node.left
                stack.extend([node.right, node.left])\
        
        return root
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
    
    
        if root:
            root.left, root.right = self.invertTree1(root.right), self.invertTree1(root.left)
        return root
            
    
    
   
