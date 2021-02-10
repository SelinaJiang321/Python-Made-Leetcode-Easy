"""


Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: true
Example 2:


Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
Example 3:

Input: root = []
Output: true
 

Constraints:

The number of nodes in the tree is in the range [0, 5000].
-104 <= Node.val <= 104

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        """
        Explanation:
        For the tree, we usually use recursion. The logic is always complicates so we better have some examples.
        Let's say we have [3,null, 5, 7,null]
        1.self.ok = True dfs(3)
        2.if 3 and True: l = dfs(null), right = dfs(5) 
        3.dfs(null) = 0 dfs(5) : r = dfs(null) = 0, l = dfs(7): return 0-> return max(0,0) + 1
        4. return max(0,1) + 1
        5. r = 2, l = 0 abs(2) > 1, self.ok = False
        
        
        
        """
        self.ok = True
        def dfs(n):
            if n and self.ok:
                l = dfs(n.left)
                r = dfs(n.right)
                
                if abs(l-r) > 1:
                    self.ok = False
                return max(l, r) + 1
            return 0
         dfs(root)
         
         return self.ok
         
         # Any comments?
         
