class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        if not position or not speed:
            return None
        for i in range(len(position)):
            cars.append([position[i],speed[i]])
        cars.sort(reverse= True)
        time = []
        for p,s in cars:
            time_taken = (target-p)/s
            time.append(time_taken)
        stack = []
        count = 0
        for current_time in time:
            if not stack:
                stack.append(current_time)
            if current_time<=stack[-1]:
                continue
            else:
                stack.append(current_time)
        return(len(stack))