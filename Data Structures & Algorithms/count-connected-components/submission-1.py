class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graphMap = {i:[] for i in range(n)}
        for a, b in edges:
            graphMap[a].append(b)
            graphMap[b].append(a)
        
        visitArr = [False] * n

        def dfs(n):
            if visitArr[n]:
                return
            
            visitArr[n] = True
            for nei in graphMap[n]:
                if not visitArr[nei]:
                    dfs(nei)
        comp = 0
        for i in range(n):
            if not visitArr[i]:
                dfs(i)
                comp += 1
        return comp
        