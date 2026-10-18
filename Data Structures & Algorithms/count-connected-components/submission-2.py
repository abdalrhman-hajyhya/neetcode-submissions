class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graphMap = {i:[] for i in range(n)}
        for a, b in edges:
            graphMap[a].append(b)
            graphMap[b].append(a)
        
        visitArr = [False] * n

        def bfs(node):
            queue = deque()
            queue.append(node)
            while queue:
                nextNode = queue.popleft()
                visitArr[nextNode] = True
                for nei in graphMap[nextNode]:
                    if not visitArr[nei]:
                        queue.append(nei)
        comp = 0
        for i in range(n):
            if not visitArr[i]:
                bfs(i)
                comp += 1
        return comp
        