class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(char for char in s if char.isalnum()).lower()
        i = len(s) - 1
        j = 0

        
        while(i > j):
            if s[i] != s[j]:
                return False
            i -= 1
            j += 1

        return True
        