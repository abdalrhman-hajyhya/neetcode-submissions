class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        maxArea = 0
        visit = set()
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        def bfs(row,col):
            queue = collections.deque()
            visit.add((row,col))
            queue.append((row,col))
            islandArea = 1
            while queue:
                cellRow, cellCol = queue.popleft()
                for addRow, addCol in directions:
                    r, c = cellRow + addRow, cellCol + addCol
                    if r >= 0 and r < rows and c >= 0 and c < cols and (r,c) not in visit and grid[r][c] == 1:
                        queue.append((r,c))
                        visit.add((r,c))
                        islandArea += 1
            return islandArea
        for row in range(rows):
            for col in range(cols):
                if (row, col) not in visit and grid[row][col] == 1:
                    maxArea = max(bfs(row,col), maxArea)
        return maxArea