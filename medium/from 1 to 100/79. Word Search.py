"""

Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

Example 1:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
Example 2:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
Example 3:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
 

Constraints:

m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.
 

Follow up: Could you use search pruning to make your solution faster with a larger board?


"""

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        #DFS
        if not board : return False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.depthFirstSearch(board,i,j,word):
                    return True
        return False
        
    def depthFirstSearch(self,board,i, j,word):
        if len(word) == 0: return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or word[0] != board[i][j]:
            return False
        tmp = board[i][j]
        board[i][j] = '*'
        res = self.depthFirstSearch(board,i-1,j,word[1:]) or self.depthFirstSearch(board,i,j-1,word[1:]) or self.depthFirstSearch(board,i+ 1,j,word[1:]) or self.depthFirstSearch(board,i,j+ 1,word[1:])
        board[i][j] = tmp

        return res

            
            
            
        
