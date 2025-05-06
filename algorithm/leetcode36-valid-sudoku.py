from collections import defaultdict
from typing import List


# Hash Set
# board 요소를 루프돌때마다 해당하는 row, column, squares에 반복되는 value가 있는지를 체크한다.
# square는 3x3으로 나누어져 있기 때문에 현재 row, column에 3을 나눈 몫을 활용하여 key를 만든다.
# ex) row = 4, column = 5 -> squareKey = (4 // 3, 5 // 3) = (1, 1)
# Time complexity: O(n2), 단 board의 크키가 9x9로 고정이므로 O(1)로 볼 수 있다.
# Space complexity: O(n2), 단 board의 크키가 9x9로 고정이므로 O(1)로 볼 수 있다.
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for row in range(9):
            for col in range(9):
                boardVal = board[row][col]

                if boardVal == ".":
                    continue

                squareKey = (row // 3, col // 3)

                if (
                    boardVal in rows[row]
                    or boardVal in cols[col]
                    or boardVal in squares[squareKey]
                ):
                    return False

                rows[row].add(boardVal)
                cols[col].add(boardVal)
                squares[squareKey].add(boardVal)

        return True
