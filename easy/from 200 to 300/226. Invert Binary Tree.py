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
        # create a new stack
        # the head of the stack points to the root of the tree
        # stack in python is built on a linked list structure
        stack = [root]
        while stack:
            # pops out the "head" of the tree
            node = stack.pop()
            # if node is not NULL
            if node:
                # invert the left and the right of the "head"
                node.left,node.right = node.right, node.left
                # link the node.right and node.left to the "head" stack
                stack.extend([node.right, node.left])
        
        return root
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
     
        # invert the "leaf" of the root already
        if root:
            root.left, root.right = self.invertTree1(root.right), self.invertTree1(root.left)
        return root
            
    
    
   
