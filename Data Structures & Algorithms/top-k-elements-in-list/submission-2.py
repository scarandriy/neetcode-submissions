from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        lst = sorted(count, key = count.get, reverse = True)
        res = []
        for i in range(k):
            res.append(lst[i])
            if len(res) == k:
                return res