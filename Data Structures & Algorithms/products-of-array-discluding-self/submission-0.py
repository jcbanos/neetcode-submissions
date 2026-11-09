class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        
        for i in range(len(nums)):
            if i == 0:
                prefix[0] = nums[0]
            else:
                prefix[i] = nums[i] * prefix[i-1]
        
        suffix = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                suffix[i] = nums[len(nums) - 1]
            else:
                suffix[i] = nums[i] * suffix[i + 1]

        multiplications = []

        for i in range(len(nums)):
            if i == 0:
                multiplications.append(suffix[1])
            elif i == len(nums) - 1:
                multiplications.append(prefix[i - 1])
            else:
                multiplications.append(prefix[i-1] * suffix[i+1])
        
        
        return multiplications
            

        