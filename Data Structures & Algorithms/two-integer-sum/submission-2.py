class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_map = {}

        for index, num in enumerate(nums):
            if num in index_map:
                index_map[num].append(index)
            else:
                index_map[num] = [index]
        
        for index, num in enumerate(nums):
            if target - num in index_map:
                for i in index_map[target-num]:
                    if i != index:
                        return [index, i]
        
        return []
            
            
        