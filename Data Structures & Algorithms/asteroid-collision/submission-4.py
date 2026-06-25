class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for current in asteroids:
            while stack and stack[-1] > 0 and current < 0:
                if stack[-1] == -current:
                    stack.pop()
                    break
                elif stack[-1] < -current:
                    stack.pop()
                else:
                    break
            else:
                stack.append(current)
        return stack