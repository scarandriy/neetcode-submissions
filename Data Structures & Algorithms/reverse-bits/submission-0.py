class Solution:
    def reverseBits(self, n: int) -> int:
        res = format(n, '032b')
        return int(res[::-1], 2)