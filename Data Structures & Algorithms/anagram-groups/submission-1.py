class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) < 0:
            return []

        groups = {}
        for string in strs:
            letter_counts = [0] * 26
            for char in string:
                index = ord(char) - ord('a')
                letter_counts[index] += 1
            
            count_string = ",".join(str(n) for n in letter_counts)

            if count_string in groups:
                groups[count_string].append(string)
            else:
                groups[count_string] = [string]
        
        answer = []
        for key, value in groups.items():
            answer.append(value)
        
        return answer



            




        

        


        

                
                




        

        

                



        