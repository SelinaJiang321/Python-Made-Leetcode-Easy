"""

Given a binary search tree, return a balanced binary search tree with the same node values.

A binary search tree is balanced if and only if the depth of the two subtrees of every node never differ by more than 1.

If there is more than one answer, return any of them.

 

Example 1:



Input: root = [1,null,2,null,3,null,4,null,null]
Output: [2,1,3,null,null,null,4]
Explanation: This is not the only correct answer, [3,1,4,null,2,null,null] is also correct.
 

Constraints:

The number of nodes in the tree is between 1 and 10^4.
The tree nodes will have distinct values between 1 and 10^5.
"""

class Solution(object):
    def balanceBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        inorder_array = []

        #build inorder traversal of the BST
        def buildArray(node):
            if not node:
                return

            buildArray(node.left)
            inorder_array.append(node.val)
            buildArray(node.right)

        #build a BST from inorder array
        def balanceBST(inorder_array):
            if not inorder_array:
                return 

            mid = len(inorder_array) // 2
            node = TreeNode(inorder_array[mid])
            node.left = balanceBST(inorder_array[ :mid ])
            node.right = balanceBST(inorder_array[mid + 1: ])

            return node

        buildArray(root)
        return balanceBST(inorder_array)
      
