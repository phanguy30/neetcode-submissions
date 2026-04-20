class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res+= str(len(s))+"#"+s
        return res


    def decode(self, s: str) -> List[str]:
        res = []
        i =0
        while i < len(s):
            j = i
            while s[j] != '#':
                j+=1
            curr_len = int(s[i:j])
            curr_word = s[j+1:j+1+curr_len]
            res.append(curr_word)
            i = j+1+curr_len
        return res



