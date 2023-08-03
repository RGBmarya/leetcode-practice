from collections import defaultdict

"""

Matching
- hashset/hashmap

Plan
- Rows and columns: iterate over each, keep track of encountered elements with a set, if new int exists in set, return False + keep adding new elements to set
- squares:
    - hashmap ((r, c) : list (r, c of 3x3 matrix) r//3, c//3
    - keep adding new elements to set, if new int exists, then return false
- return True

Evaluate
Time: O(1)
Space: O(1)
"""

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set) # (r//3, c//3) : set

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[(r//3, c//3)]:
                    return False
                elif board[r][c] != ".":
                    rows[r].add(board[r][c])
                    cols[c].add(board[r][c])
                    squares[(r//3, c//3)].add(board[r][c])
        return True
    
        
