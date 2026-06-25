class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []: return ""
        s = ""
        for x in strs:
            s += str(len(x)) + "#" + x
        return s

    def decode(self, s: str) -> List[str]:
        if s == "": return []
        i = 0 
        strs = []
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            strs.append(s[i:j])
            i = j 
        return strs



