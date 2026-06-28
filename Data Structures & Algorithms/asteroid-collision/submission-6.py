class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for current in asteroids:
            while stack and stack[-1] > 0 and current < 0:
                if abs(current) > abs(stack[-1]):
                    stack.pop()
                elif abs(current) == abs(stack[-1]):
                    stack.pop()
                    break
                else:
                    break
            else:
                stack.append(current)
        return stack