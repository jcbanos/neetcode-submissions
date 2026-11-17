class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        suffix = [1] * len(nums)
        prefix = [1] * len(nums)
        products = []

        for index, num in enumerate(nums):
            if index == 0:
                prefix[index] *= nums[index]
            else: 
                prefix[index] = nums[index] * prefix[index - 1]
            
        for index in range(len(nums) - 1, -1, -1):
            if index == len(nums) - 1:
                suffix[index] *= nums[index]
            else:
                suffix[index] = nums[index] * suffix[index + 1]

        products = [0] * len(nums)

        for i in range(len(nums)):
            if i == 0:
                products[i] = suffix[i + 1]
            elif i == len(nums) - 1:
                products[i] = prefix[i - 1]
            else:
                products[i] = prefix[i - 1] * suffix[i + 1]
        
        return products

            

        