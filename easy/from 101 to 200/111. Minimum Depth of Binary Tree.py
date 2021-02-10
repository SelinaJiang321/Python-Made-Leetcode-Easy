"""

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 2
Example 2:

Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5
 

Constraints:

The number of nodes in the tree is in the range [0, 105].
-1000 <= Node.val <= 1000

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None: return 0
		# start a queue, first in first out, this gives us a level-order traversal
        queue = deque()
		# we know we have a root, so we can add it to our queue
		# we add a tuple(node, level) so that we can track what level we are at
        queue.append((root, 1))
        
		#while there is something in our queue, keep doing the following
        while queue:
			#remove our node and retrieve the depth of the node from our queue
            node, depth = queue.popleft()
            
			#if we dont have a left or right child node then we have a leaf and we have our minimum depth!
            if not node.left and not node.right:
                return depth
            
		#if we do have the children we add them to our queue, we also know these are exactly one 
			#level deeper than our current node so we add one to our depth
            if node.left:
                queue.append((node.left, depth + 1))
            
            if node.right:
                queue.append((node.right, depth + 1))
 
    # Any comments?
                
            
