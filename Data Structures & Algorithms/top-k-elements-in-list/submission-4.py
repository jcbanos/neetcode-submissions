import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = {}

        for num in nums:
            if num not in frequencies:
                frequencies[num] = 1
            else:
                frequencies[num] += 1
        
        frequent_words = [[] for _ in range(len(nums))]

        for key, value in frequencies.items():
            frequent_words[value-1].append(key)

        answers = []

        for i in range(len(nums) - 1, -1, -1):
            for word in frequent_words[i]:
                answers.append(word)
            
            if len(answers) == k:
                return answers
        
        return answers

        
            

        

        