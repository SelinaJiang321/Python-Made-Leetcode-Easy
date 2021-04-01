"""
Given an integer n, return any array containing n unique integers such that they add up to 0.

 

Example 1:

Input: n = 5
Output: [-7,-1,1,3,4]
Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].
Example 2:

Input: n = 3
Output: [-1,0,1]
Example 3:

Input: n = 1
Output: [0]
 

Constraints:

1 <= n <= 1000

"""

class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = [0] * n
        if (n % 2 != 0):
            mid = (n-1)//2
            res[0] = -mid
            for i in range(1,n,1):
                res[i] = res[i-1] + 1
                
        else:
            mid = n //2
            res[0] = -mid
            for i in range(1,n,1):
                if (i == mid) :
                    res[i] = res[i-1] + 2
                else:
                    res[i] = res[i-1] + 1
                    
        return res
                
 """
 A simpler way by using append the element in the array
 """
class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        L, rem = n // 2, n % 2
        if rem != 0: ans = [0]
        else: ans = []
        for i in range(1,L+1):
            ans.append(-i)
            ans.append(i) 
        return ans
      
      # Take away: append the element directly without making it symmetric
