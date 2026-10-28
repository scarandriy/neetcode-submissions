class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []
        for i in range(n + 1):
            count = 0
            a = bin(i)
            for j in a:
                if j == '1':
                    count += 1
            result.append(count)
        return result 

