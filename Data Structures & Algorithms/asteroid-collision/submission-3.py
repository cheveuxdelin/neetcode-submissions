class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for current in asteroids:
            survived = True
            while stack and stack[-1] > 0 and current < 0:
                if stack[-1] == -current:
                    stack.pop()
                    survived = False
                    break
                elif stack[-1] < -current:
                    stack.pop()
                else:
                    survived = False
                    break
            if survived:
                stack.append(current)
        return stack