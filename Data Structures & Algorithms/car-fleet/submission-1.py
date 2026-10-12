class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        triples = []
        for i in range(len(position)):
            time = (target - position[i]) / speed[i]
            triples.append([position[i], speed[i], time])

        # Sort closest to target first (descending by position)
        triples.sort(key=lambda x: x[0], reverse=True)

        stack = []
        for pos, spd, time in triples:
            stack.append(time)
            # If the car behind reaches target faster/same time as car ahead, they merge
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)