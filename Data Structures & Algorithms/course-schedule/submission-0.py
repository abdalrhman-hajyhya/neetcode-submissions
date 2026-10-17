class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseMap = {i:[] for i in range(numCourses)}
        for prerequisite in prerequisites:
            a, b = prerequisite
            courseMap[a].append(b)
        visitSet = set()
        def dfs(course):
            if course in visitSet:
                return False
            if len(courseMap[course]) == 0:
                return True
            visitSet.add(course)
            for crs in courseMap[course]:
                if dfs(crs) == False:
                    return False
            visitSet.remove(course)
            courseMap[course] = []
            return True
        for i in range(numCourses):
            if dfs(i) == False:
                return False
        return True
