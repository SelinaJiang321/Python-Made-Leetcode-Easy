"""

Given a binary search tree with non-negative values, find the minimum absolute difference between values of any two nodes.

Example:

Input:

   1
    \
     3
    /
   2

Output:
1

Explanation:
The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).
 

Note:

There are at least two nodes in this BST.
This question is the same as 783: https://leetcode.com/problems/minimum-distance-between-bst-nodes/


"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        min_dist=100000000
        prev_node=None
        stack=[]
        while stack or root:
            if root:
                stack.append(root)
                root=root.left
            else:
                root=stack.pop()
                if prev_node and root.val-prev_node.val<min_dist:
                    min_dist=root.val-prev_node.val
                prev_node=root
                root=root.right
                
        return min_dist
        
