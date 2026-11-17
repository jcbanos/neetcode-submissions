class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for string in strs:
            encoded_string += str(len(string)) + ";" + string

        return encoded_string


    def decode(self, s: str) -> List[str]:
            j = 0
            strings = []
            while(j < len(s)):
                number_of_chars_string = ""
                while(s[j] != ";"):
                    number_of_chars_string += s[j]
                    j += 1
                number_of_chars = int(number_of_chars_string)
                j += 1
                actual_string = ""
                string_start_index = j
                while(j < string_start_index + number_of_chars):
                    actual_string += s[j]
                    j += 1
                strings.append(actual_string)
            return strings