class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_anagrams = {}

        for word in strs:
            word_array = [0] * 26
            for char in word:
                word_array[ord(char) - ord('a')] += 1
            
            word_hash = ":".join([str(x) for x in word_array])

            if word_hash in word_anagrams:
                word_anagrams[word_hash].append(word)
            else:
                word_anagrams[word_hash] = [word]
        
        answer = []

        for index, value in word_anagrams.items():
            answer.append(value)
        
        return answer
                



            




        

        


        

                
                




        

        

                



        