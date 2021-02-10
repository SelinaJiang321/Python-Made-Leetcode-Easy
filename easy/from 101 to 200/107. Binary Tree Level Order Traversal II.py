"""

Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]


"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        if not root: return None
        
        else:
        """
        Explanation:
        Suppose we have [3,9,20,null, null,15,null]
        1.q.append(3)-> q:[3] lenq(3) =1 >0 temp = 3 q.append(9) q.append(20)res.append(3) so hold is to store the pop value, q = [9,20]
        2. len(q) = 2 > 0 temp =20 hold = 20 q.append(15) res.append(20) so  res = [[3],[20]]
        3. temp = 9= hold, res = [[3],[20,9]], q=[15]
        4. temp = 15 = hold res.append(15) res = [[3],[20,9],[15]]
        5. res[::-1] = [[15],[20,9],[3]]
        
        """
          res = []
          q = []
          q.append(root)
          
          while len(q)>0:
              hold = []
              for i in range(len(q)):
                  temp = q.pop(0)
                  hold.append(temp)
                  if temp.left:
                      q.append(temp.left)
                  if temp.right:
                      q.append(temp.right)
              res.append(hold)
          
          return res[::-1]
          
          # Any comments?
          
