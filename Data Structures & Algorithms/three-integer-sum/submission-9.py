class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        index = 0
        results = []

        sorted_nums = sorted(nums)

        while(index < len(nums)):
            if sorted_nums[index - 1] == sorted_nums[index] and index != 0:
                index += 1
                continue
            l = index + 1
            r = len(sorted_nums) - 1
            while(l < r):
                three_sum = sorted_nums[index] + sorted_nums[l] + sorted_nums[r]
                if three_sum < 0:
                    l += 1
                elif three_sum > 0:
                    r -= 1
                else:
                    results.append([sorted_nums[index], sorted_nums[l], sorted_nums[r]])
                    l += 1
                    while(l < r and sorted_nums[l] == sorted_nums[l - 1]):
                        l += 1
            index += 1

        return  results



        

        
        