class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for x in strs:
            res += str(len(x)) + "#" + x
        return res
    
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while j < len(s) and s[j] != "#":
                j += 1
            length = int(s[i:j])
            j += 1
            word = s[j:j+length]
            res.append(word)
            i = j + length

        return res



