import typing
# standard solution compression
# the cars that catch up need to absorb the slower cars in the way
# strictly decreasing speeds looking stack
# we need to find the next greater speed

class CarFleet(typing.NamedTuple):
    time_to_arrive: float
    n_cars: int

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack: list[CarFleet] = []

        # do we need to sort?
        # is there a specific order we want to be processing them?
        # how can i know this??
        # we do want to sort by positions
        # since that solves half of the variable
        # for us to be able to just rely on the time to time_to_arrive
        sorted_cars = sorted(zip(position, speed))

        for car_position, car_speed in sorted_cars:
            # self car is a possible fleet
            count = 1
            time_to_arrive = (target - car_position) / car_speed
            while stack and stack[-1].time_to_arrive <= time_to_arrive:
                count += stack.pop().n_cars
            stack.append(CarFleet(time_to_arrive, count))

        return len(stack)