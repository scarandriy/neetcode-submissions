class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        numeric = {}
  
        for s in strs:
            key = "".join(sorted(s))
            if key in numeric:
                numeric[key].append(s)
            else:
                numeric[key] = [s]
        res = []
        for val in numeric.values():
            res.append(val)
        return res
            