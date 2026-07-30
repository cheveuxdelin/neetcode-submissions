# its saying that its guaranteed that at most one solution exists
# then why is it saying that if impossible, return -1? contradicting
# no, its saying that its either 0 or 1 solution
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # we can help ourselves by computing an array of
        # net gain on gas for each index
        n = len(gas)
        net_gain = [g-c for g, c in zip(gas, cost)]
        # if its guaranteed that a solution exists,
        # we just gotta start at the biggest starting gain
        # that will give us the highest starting fuel
        # not only that, also we need to check if
        # the sum of all gains is bigger than 0
        if sum(net_gain) < 0:
            return -1

        # now we know there's gonna be a solution
        current_tank = 0
        starting_station = 0
        for i in range(n):
            current_tank += net_gain[i]

            if current_tank < 0:
                starting_station = i+1
                current_tank = 0
        return starting_station




