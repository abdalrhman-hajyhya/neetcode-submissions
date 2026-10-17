class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #step one: building the graph
        graph = {i:[] for i in range(numCourses)}
        inDegrees = [0] * numCourses
        for prerequisite in prerequisites:
            a, b = prerequisite
            graph[a].append(b)
            inDegrees[b] += 1
        
        #step two: appending the zero inDegree nodes
        queue = deque([i for i in range(numCourses) if inDegrees[i] == 0])
        
        #step three: poping from the queue and adding to the topological array
        topologicalSortedArr = []
        while queue:
            node = queue.pop()
            topologicalSortedArr.append(node)

            #step four: checking if any neighbors become of degree zero
            for neighbor in graph[node]:
                inDegrees[neighbor] -= 1
                if inDegrees[neighbor] == 0:
                    queue.append(neighbor)

        #step five: checking if the condition for the topological sort have been satisfied
        return len(topologicalSortedArr) == numCourses 