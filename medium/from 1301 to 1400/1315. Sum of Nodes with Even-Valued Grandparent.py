"""

Given a binary tree, return the sum of values of nodes with even-valued grandparent.  (A grandparent of a node is the parent of its parent, if it exists.)

If there are no nodes with an even-valued grandparent, return 0.

 

Example 1:



Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
Output: 18
Explanation: The red nodes are the nodes with even-value grandparent while the blue nodes are the even-value grandparents.
 

Constraints:

The number of nodes in the tree is between 1 and 10^4.
The value of nodes is between 1 and 100.

"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumEvenGrandparent(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def bfs(root):
            q = deque([(root,None,None)])
            current = root
            ans = 0
            while True:
                nodecount = len(q)
                if nodecount == 0: break
                while nodecount:
                    node = q.popleft()
                    current = node[0]
                    parent = node[1]
                    grandparent = node[2]
                    
                    if grandparent is not None and grandparent.val%2 == 0:
                        ans += current.val 
                    
                    if current.left:
                        q.append((current.left,current,parent))
                    if current.right:
                        q.append((current.right,current,parent))
                    nodecount -= 1
            return ans
        return bfs(root)
