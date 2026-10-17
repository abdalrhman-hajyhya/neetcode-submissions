class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        freshFruit, time = 0, 0
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    freshFruit += 1
                if grid[row][col] == 2:
                    queue.append((row,col))
        
        while queue and freshFruit > 0:
            iterations = len(queue)
            for i in range(iterations):
                r, c = queue.popleft()
                for addRow, addCol in directions:
                    nextRow, nextCol = r + addRow, c + addCol
                    if 0 <= nextRow < rows and 0 <= nextCol < cols and grid[nextRow][nextCol] == 1:
                        grid[nextRow][nextCol] = 2
                        queue.append((nextRow,nextCol))
                        freshFruit -= 1
            time += 1
        return time if freshFruit == 0 else -1