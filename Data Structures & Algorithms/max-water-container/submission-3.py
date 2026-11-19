class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1

        max_area_so_far = min((heights[l], heights[r])) * (r - l)

        while(l < r):
            if heights[l] >= heights[r]:
                r -= 1
            else:
                l += 1
            
            if min((heights[l], heights[r])) * (r - l) > max_area_so_far:
                max_area_so_far = min((heights[l], heights[r])) * (r - l)

        return max_area_so_far

        