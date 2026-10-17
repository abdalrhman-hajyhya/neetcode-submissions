class Solution:
    def islandsAndTreasure(self, grid: list[list[int]]) -> None:
        if not grid:
            return
        
        from collections import deque
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        visit = set()
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    queue.append((row,col))
                    visit.add((row,col))
                    
        distance = 0
        while queue:
            iterations = len(queue)
            for i in range(iterations):
                row, col = queue.popleft()
                
                for addRow, addCol in directions:
                    r, c = row + addRow, col + addCol
                    
                    if 0 <= r < rows and 0 <= c < cols and (r,c) not in visit and grid[r][c] != -1:
                        grid[r][c] = distance + 1
                        visit.add((r,c))    
                        queue.append((r,c))               
            distance += 1