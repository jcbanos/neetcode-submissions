class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        frequencies_s = {}
        frequencies_t = {}

        if len(s) != len(t):
            return False

        for char in s:
            if char in frequencies_s:
                frequencies_s[char] += 1
            else:
                frequencies_s[char] = 1
        
        for char in t:
            if char in frequencies_t:
                frequencies_t[char] += 1
            else:
                frequencies_t[char] = 1
        
        for key, value in frequencies_s.items():
            if key not in frequencies_t or frequencies_t[key] != value:
                return False
        
        return True
