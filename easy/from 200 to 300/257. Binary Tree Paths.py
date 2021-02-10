"""

Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:

Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        
        # recursive version
        if not root: return []
        if not root.right and not root.left: return [str(root.val)]
        
        treepath = [str(root.val) + '->' + path for path in self.binaryTreePaths(root.left)]
        treepath += [str(root.val) + '->' + path for path in self.binaryTreePaths(root.right)]
        
        return treepath
        
        # Maybe it's easier to use stack
        # Any comments?
        
