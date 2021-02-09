"""

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 

Constraints:

1 <= n <= 45

"""

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return n
        
        # thinking backward-> if there are n steps, we need to process it either recursively or iterately
        # so this is Fibonacchi problem then, we need to calculate the sum of each step
        
        a,b,res = 1,2,0
        for i in range(3, n + 1, 1):
            res = a + b
            a,b = b, res
        return res
        
         #Time Complexity: O(1) Space Complexity: O(n)
