class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry_over = 1
        
        for i in range(len(digits)-1, -1, -1):
            div, mod = divmod(digits[i]+carry_over, 10)
            carry_over = div
            digits[i] = mod
            if not carry_over:
                break

        if carry_over:
            return [1] + digits
        else:
            return digits