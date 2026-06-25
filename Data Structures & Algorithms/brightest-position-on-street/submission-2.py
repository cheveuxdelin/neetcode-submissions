class Solution:
    def brightestPosition(self, lights: List[List[int]]) -> int:
        events = []
        for position, range_of_light in lights:
            events.append((position - range_of_light, 1))
            events.append((position + range_of_light + 1, -1))
        
        events.sort()

        max_light_position = -1
        max_light = 0
        current_light = 0

        for position, change in events:
            current_light += change
            if current_light > max_light:
                max_light = current_light
                max_light_position = position
        return max_light_position

