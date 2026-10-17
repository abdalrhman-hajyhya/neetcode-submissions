class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        maxArea = 0
        visit = set()
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        def dfs(row, col):
            if row >= rows or row < 0 or col >= cols or col < 0 or grid[row][col] == 0 or (row,col) in visit:
                return 0
            visit.add((row,col))
            return (1 + dfs(row + 1, col) + dfs(row - 1, col) + dfs(row, col + 1) + dfs(row, col - 1))
        for row in range(rows):
            for col in range(cols):
                if (row, col) not in visit and grid[row][col] == 1:
                    maxArea = max(dfs(row, col), maxArea)
        return maxArea