## time comp - O(m*n*3^k), space comp - O(K)

class Solution:
    def getMaximumGold(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        def collect_gold(row: int, col: int) -> int:
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return 0
            if grid[row][col] == 0:
                return 0

            current_gold = grid[row][col]
            grid[row][col] = 0

            up = collect_gold(row - 1, col)
            down = collect_gold(row + 1, col)
            left = collect_gold(row, col - 1)
            right = collect_gold(row, col + 1)

            grid[row][col] = current_gold

            return current_gold + max(up, down, left, right)

        max_gold = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] > 0:
                    gold_from_here = collect_gold(row, col)
                    max_gold = max(max_gold, gold_from_here)

        return max_gold