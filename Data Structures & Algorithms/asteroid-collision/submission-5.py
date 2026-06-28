
# what happens with zero asteroids?
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for current in asteroids:
            is_destroyed = False
            while stack and not is_destroyed and (is_colliding := stack[-1] > 0 and current < 0):
                if abs(current) == abs(stack[-1]):
                    stack.pop()
                    is_destroyed = True
                elif abs(current) < abs(stack[-1]):
                    is_destroyed = True
                else:
                    stack.pop()
            
            if not is_destroyed:
                stack.append(current)
        return stack