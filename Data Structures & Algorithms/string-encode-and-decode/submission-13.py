class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []: return ""
        s = ""
        for x in strs:
            s += str(len(x)) + "#" + x
        return s

    def decode(self, s: str) -> List[str]:
        i = 0 
        j = 0
        sol = []
        while i < len(s):
            while s[j] != "#":
                j += 1
            length = s[i:j]
            i = j + 1
            j = i + int(length)
            sol.append(s[i:j])
            i = j 
        return sol



