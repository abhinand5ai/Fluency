class Solution:
    def trap(self, height: list[int]) -> int:
        n = len(height)
        if n == 0:
            return 0
        rMax = [-1] * n
        lMax = -1
        for i in range(1, n):
            rMax[n - i - 1] = max(height[n - i], rMax[n - i])
        water = [0] * n
        for i in range(n):
            water[i] = max(0, min(rMax[i], lMax) - height[i])
            lMax = max(lMax, height[i])
        return sum(water)


def main():
    sol = Solution()
    total_water = sol.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
    print(total_water)


if __name__ == '__main__':
    main()
