import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_array = [0]*2001

        for num in nums:
            num_array[num + 1000] += 1

        top_k = []

        top_k = heapq.nlargest(k, enumerate(num_array), key=lambda x: x[1])

        final_values = []

        for i in top_k:
            final_values.append(i[0]-1000)
        
        return final_values

        
            

        

        