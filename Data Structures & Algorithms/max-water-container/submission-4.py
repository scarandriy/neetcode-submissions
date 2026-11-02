class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # max_area = 0
        # for i in range(len(heights)):
        #     for j in range(i, len(heights)):
        #         max_area = max(max_area, (j - i) * min(heights[i], heights[j]))
        # return max_area
        res = 0
        l, r = 0, len(heights) - 1
        while l < r:
            area = (r - l) * min(heights[l], heights[r])
            res = max(area, res)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return res