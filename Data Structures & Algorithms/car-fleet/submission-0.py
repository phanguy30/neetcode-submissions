class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # 1. Combine position and speed, then calculate time for each car
        # We pair (position, speed) so we can sort by starting position
        cars = []
        for i in range(len(position)):
            time = (target - position[i]) / speed[i]
            cars.append((position[i], time))
        
        # 2. Sort by position descending (cars closest to the target first)
        cars.sort(key=lambda x: x[0], reverse=True)
        
        stack = []
        for pos, time in cars:
            # 3. If the current car takes MORE time than the fleet in front,
            # it cannot catch up. It becomes the leader of a new fleet.
            if not stack or time > stack[-1]:
                stack.append(time)
            
            # If time <= stack[-1], the car catches up and joins the fleet.
            # We don't need to add it to the stack because it's limited 
            # by the slower car in front.
                
        return len(stack)

        