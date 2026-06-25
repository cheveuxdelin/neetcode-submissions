class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        current = [0, 0]

        for bill in bills:
            if bill == 5:
                current[1] += 1
            elif bill == 10:
                if current[1]:
                    current[0] += 1
                    current[1] -= 1
                else:
                    return False
            else:
                if current[0] and current[1]:
                    current[0] -= 1
                    current[1] -= 1
                elif current[1] >= 3:
                    current[1] -= 3
                else:
                    return False
        return True
