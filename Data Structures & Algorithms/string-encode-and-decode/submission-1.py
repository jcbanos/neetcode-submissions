class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return "ö"
        return "ü".join(strs)

    def decode(self, s: str) -> List[str]:
        if s == "ö":
            return []
        return s.split("ü")
