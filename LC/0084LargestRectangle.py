class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        heights.insert(0, 0)
        heights.append(0)
        n = len(heights)
        nearestRight = [0] * n
        nearestLeft = [0] * n
        stkR = []
        stkL = []

        for i in range(n):
            while stkR and heights[stkR[-1]] >= heights[n - i - 1]:
                stkR.pop()
            nearestRight[n - i - 1] = (stkR[-1] - n + i + 1) if stkR else 0
            stkR.append(n - i - 1)
            while stkL and heights[stkL[-1]] >= heights[i]:
                stkL.pop()
            nearestLeft[i] = (i - stkL[-1]) if stkL else 0
            stkL.append(i)

        return max(heights[i] * (nearestRight[i] + nearestLeft[i] - 1) for i in range(n))
