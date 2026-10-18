class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.components = n
    def find(self, n):
        current = n
        while current != self.parent[current]:
            self.parent[current] = self.parent[self.parent[current]]
            current = self.parent[current]
        return current
    def union(self, a, b):
        rootOfA = self.find(a)
        rootOfB = self.find(b)
        if rootOfA == rootOfB:
            return False
        if self.rank[rootOfA] > self.rank[rootOfB]:
            self.parent[rootOfB] = rootOfA
        elif self.rank[rootOfA] < self.rank[rootOfB]:
            self.parent[rootOfA] = rootOfB
        else:
            self.parent[rootOfA] = rootOfB
            self.rank[rootOfB] += 1
        
        self.components -= 1
        return True

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        n = DSU(n)
        for a, b in edges:
            n.union(a, b)
        return n.components
        