import typing
# standard solution compression
# the cars that catch up need to absorb the slower cars in the way
# strictly decreasing speeds looking stack
# we need to find the next greater speed

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack: list[float] = []

        # do we need to sort?
        # is there a specific order we want to be processing them?
        # how can i know this??
        # we do want to sort by positions
        # since that solves half of the variable
        # for us to be able to just rely on the time to time_to_arrive

        # we dont need to answer the size of the fleets
        # so we can just have the time to arrive
        sorted_cars = sorted(zip(position, speed), reverse=True)

        for car_position, car_speed in sorted_cars:
            time_to_arrive = (target - car_position) / car_speed

            if not stack or time_to_arrive > stack[-1]:
                stack.append(time_to_arrive)
        return len(stack)