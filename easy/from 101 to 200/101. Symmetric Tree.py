"""


Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
 

But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3
 

Follow up: Solve it both recursively and iteratively.


"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        if not root:
            return True
            
        def isMirror(tree1, tree2):
            if not tree1 or not tree2:
                # to judge whether tree1 == tree2 == None
                return tree1 == tree2
            if tree1.val != tree2.val:
                return False
            # to check if the tree is symmetric
            return self.isMirror(tree1.left,tree2.right) and self.isMirror(tree2.left,tree2.right)
        # start the recursion
        return isMirror(tree.left,tree.right)
        
        
