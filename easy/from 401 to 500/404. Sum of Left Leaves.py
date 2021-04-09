"""

Given the root of a binary tree, return the sum of all left leaves.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 24
Explanation: There are two left leaves in the binary tree, with values 9 and 15 respectively.
Example 2:

Input: root = [1]
Output: 0
 

Constraints:

The number of nodes in the tree is in the range [1, 1000].
-1000 <= Node.val <= 1000

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: 
            return 0
        self.res = 0
    
        def dfs(root, isLeaf):
            if not root: 
                return

            if not root.left and not root.right and isLeaf:
                self.res += root.val

            dfs(root.left, True)
            dfs(root.right, False)

        # dfs value to search for the sum of the left tree
        dfs(root, False) 
        return self.res
        
