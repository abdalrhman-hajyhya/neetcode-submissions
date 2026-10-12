class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        times = [0] * len(position)
        for i in range(len(position)):
            times[i] = (target - position[i])/speed[i]
        
        triples = []
        for i in range(len(position)):
            triples.append([position[i],speed[i],times[i]])
        
        triples.sort(key=lambda x: x[0])

        fleet = len(position)
        stack = []

        for i in range(len(position)):
            while stack and stack[-1][2] <= triples[i][2]:
                stack.pop()
                fleet -=1
            stack.append(triples[i])
        
        return fleet
        