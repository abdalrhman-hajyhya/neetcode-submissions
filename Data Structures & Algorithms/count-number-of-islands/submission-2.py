class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        numberOfIslands = 0
        visit = set()
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        def bfs(row,col):
            queue = collections.deque()
            queue.append((row,col))
            while queue:
                nodeRow, nodeCol = queue.pop()
                for addRow, addCol in directions:
                    r, c = nodeRow + addRow, nodeCol + addCol
                    if r >= 0 and r < rows and c >= 0 and c < cols and grid[r][c] == "1" and (r,c) not in visit:
                        queue.append((r,c))
                        visit.add((r,c))

        for row in range(rows):
            for col in range(cols):
                if (row,col) not in visit and grid[row][col] == "1":
                    bfs(row,col)
                    numberOfIslands += 1
        return numberOfIslands