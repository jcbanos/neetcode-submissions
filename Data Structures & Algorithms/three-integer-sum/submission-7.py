class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        sorted_nums = sorted(nums)

        triplets = []

        for i, num in enumerate(sorted_nums):
            if i > 0 and sorted_nums[i] == sorted_nums[i - 1]:
                continue
            left, right = i + 1, len(sorted_nums) - 1
            while left < right:
                three_sum = num + sorted_nums[left] + sorted_nums[right]
                if three_sum < 0:
                    left += 1
                elif three_sum > 0:
                    right -= 1
                else:
                    triplets.append([num, sorted_nums[left], sorted_nums[right]])
                    left += 1
                    right -= 1
                    while(sorted_nums[left] == sorted_nums[left-1] and left < right):
                        left += 1


        return triplets



        

        
        