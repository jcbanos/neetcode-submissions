class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        numbers = {}

        for num in nums:
            if num not in numbers:
                numbers[num] = True
        
        longest_sequence = 1
        for num in nums:
            current_count = 1
            if num -  1 not in numbers:
                while(num + 1 in numbers):
                    num += 1
                    current_count += 1
            if current_count > longest_sequence:
                longest_sequence = current_count
        
        return longest_sequence

        