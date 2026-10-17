class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        numberOfIslands = 0
        def dfs(row, col):
            if row >= rows or col >= cols or row < 0 or col < 0 or (row,col) in visited or grid[row][col] == "0":
                return
            
            visited.add((row,col))
            dfs(row + 1,col)
            dfs(row - 1,col)
            dfs(row,col + 1)
            dfs(row,col - 1)
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row,col) not in visited:
                    dfs(row,col)
                    numberOfIslands += 1
        return numberOfIslands