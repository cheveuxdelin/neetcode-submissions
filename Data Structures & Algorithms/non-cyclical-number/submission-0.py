class Solution:
    def isHappy(self, n: int) -> bool:

        def get_next_number(x: int):
            number_string = str(x)
            result = 0
            for c in number_string:
                result += int(c)**2
            return result

        
        slow = get_next_number(n)
        fast = get_next_number(get_next_number(n))

        while slow != fast:
            slow = get_next_number(slow)
            fast = get_next_number(get_next_number(fast))
        
        return fast == 1