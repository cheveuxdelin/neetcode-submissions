class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        # result = number of happy users before change + max number of replacements done possible

        number_of_happy_costumers = 0
        for customer, is_grumpy in zip(customers, grumpy):
            if not is_grumpy:
                number_of_happy_costumers += customer

        max_value_from_replacing = 0
        current = 0
        i = 0

        for j in range(len(customers)):
            if grumpy[j]:
                current += customers[j]

            if j >= minutes:
                if grumpy[i]:
                    current -= customers[i]
                i += 1
            if j >= minutes - 1:
                max_value_from_replacing = max(max_value_from_replacing, current)
        return number_of_happy_costumers + max_value_from_replacing
