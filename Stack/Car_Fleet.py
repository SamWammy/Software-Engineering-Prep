class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed=[]
        stack=[]
        for i in range(len(position)): 
            pos_speed.append((position[i],speed[i]))
        pos_speed.sort()
        pos_speed.reverse()

        for p,s in pos_speed: 
            arrival= (target-p)/s
            if not stack or stack[-1] < arrival: 
                stack.append(arrival)
        return len(stack)