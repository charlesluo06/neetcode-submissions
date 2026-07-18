class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p,s] for p, s in zip(position, speed)]

        stack = []
        for p, s in sorted(pair)[::-1]:
            stack.append((target - p) / s) #compute time for a car
            if len(stack) >= 2 and stack[-1] <= stack[-2]: #if time of top of behind car faster than car in front, they collide
                stack.pop()
        return len(stack)