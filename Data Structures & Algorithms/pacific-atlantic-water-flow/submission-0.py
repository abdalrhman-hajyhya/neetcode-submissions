class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])

        pacificReachable = [[False] * cols for i in range(rows)]
        atlanticReachable = [[False] * cols for i in range(rows)]

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        def bfs(sources, reachableMatrix):
            queue = deque()
            for source in sources:
                queue.append(source)
            
            while queue:
                iterations = len(queue)
                for i in range(iterations):
                    row, col = queue.popleft()
                    reachableMatrix[row][col] = True
                    for addRow, addCol in directions:
                        nextRow, nextCol = row + addRow, col + addCol
                        if 0 <= nextRow < rows and 0 <= nextCol < cols and not reachableMatrix[nextRow][nextCol] and heights[row][col] <= heights[nextRow][nextCol]:
                            queue.append((nextRow, nextCol))
        
        pacificSources = []
        for i in range(cols):
            pacificSources.append((0,i))
        for i in range(rows):
            pacificSources.append((i,0))
        atlanticSources = []
        for i in range(cols):
            atlanticSources.append((rows - 1,i))
        for i in range(rows):
            atlanticSources.append((i,cols - 1))
        bfs(pacificSources, pacificReachable)
        bfs(atlanticSources, atlanticReachable)

        res = []

        for row in range(rows):
            for col in range(cols):
                if  pacificReachable[row][col] == True and atlanticReachable[row][col] == True:
                    res.append([row,col]) 
        return res
