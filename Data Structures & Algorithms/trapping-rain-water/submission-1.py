class Solution:
    def trap(self, height: List[int]) -> int:
        trapped_water = [0] * len(height)

        l = 0
        r = len(height) - 1

        maximum_l_array = [0] * len(height)

        maximum_l = 0

        for i in range(len(height)):
            if i == 0:
                maximum_l = height[i]
                continue
            maximum_l_array[i] = maximum_l
            if height[i] > maximum_l:
                maximum_l = height[i]
        
        maximum_r_array = [0] * len(height)

        maximum_r = 0

        for i in range(len(height) - 1, -1, -1):
            if i == len(height) - 1:
                maximum_r = height[i]
                continue
            maximum_r_array[i] = maximum_r
            if height[i] > maximum_r:
                maximum_r = height[i]
        

        for i in range(len(height)):
            if height[i] < maximum_l_array[i] and height[i] < maximum_r_array[i]:
                trapped_water[i] = min(maximum_l_array[i], maximum_r_array[i]) - height[i]

        total = 0
        for i in trapped_water:
            total += i
        
        return total
        
                
            


        