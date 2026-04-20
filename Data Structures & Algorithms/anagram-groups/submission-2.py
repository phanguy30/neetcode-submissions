class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            sig = [0]*26
            for c in s:
                idx = ord(c) - ord('a')
                sig[idx]+=1
            res[tuple(sig)].append(s)
        return list(res.values())