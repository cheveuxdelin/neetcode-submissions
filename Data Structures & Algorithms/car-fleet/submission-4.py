class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [*zip(position, speed)]
        cars.sort(key = lambda x: x[0], reverse=True)

        stack = []

        for car_position, car_speed in cars:
            time_to_arrive = (target - car_position) / car_speed

            if not stack or time_to_arrive > stack[-1]:
                stack.append(time_to_arrive)
        
        return len(stack)
