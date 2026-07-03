class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        i = 0
        j = len(people) - 1
        result = 0

        while i <= j:
            if people[i] + people[j] > limit:
                j -= 1
            else:
                i += 1
                j -= 1
            result += 1
        return result