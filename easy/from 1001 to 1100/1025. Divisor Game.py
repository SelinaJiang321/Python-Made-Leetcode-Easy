"""
Alice and Bob take turns playing a game, with Alice starting first.

Initially, there is a number n on the chalkboard. On each player's turn, that player makes a move consisting of:

Choosing any x with 0 < x < n and n % x == 0.
Replacing the number n on the chalkboard with n - x.
Also, if a player cannot make a move, they lose the game.

Return true if and only if Alice wins the game, assuming both players play optimally.

 

Example 1:

Input: n = 2
Output: true
Explanation: Alice chooses 1, and Bob has no more moves.
Example 2:

Input: n = 3
Output: false
Explanation: Alice chooses 1, Bob chooses 1, and Alice has no more moves.
 

Constraints:

1 <= n <= 1000

"""

class Solution(object):
    def divisorGame(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def can_win(n,cache):
            if n <= 1:
                return False
            
            if cache[n] is not None:
                return cache[n]
            
            for x in range(1, n/2 + 1):
                if n % x == 0:
                    if not can_win(n-x,cache):
                        cache[n] = True
                        return True
            cache[n] = False
            return False
        
        #memoization
        #use boolean[] as cache
        cache = []
        for _ in range(n+1):
            cache.append(None)

            
        return can_win(n,cache)
        

        
