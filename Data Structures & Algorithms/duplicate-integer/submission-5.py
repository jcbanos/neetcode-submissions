class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        frequencies = {}

        for num in nums:
            if num not in frequencies:
                frequencies[num] = 1
            else:
                frequencies[num] += 1
        
        for key, value in frequencies.items():
            if value > 1:
                return True
        
        return False
            
        