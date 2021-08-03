class Solution:
    def stoneGameVII(self, stones: list[int]) -> int:
        initSum = sum(stones)
        n = len(stones)
        dp = {}

        def removeStones(i: int, j: int, player: str, currSum: int) -> tuple[int, int]:
            key = (i, j, player)
            if key in dp:
                return dp[key]
            if i > j:
                return 0, 0
            if player == "A":
                scores = [(removeStones(i, j - 1, "B", currSum - stones[j]), j),
                          (removeStones(i + 1, j, "B", currSum - stones[i]), i)]
                tup, ch = max(scores, key=lambda tp: tp[0][0] - tp[0][1] + currSum - stones[tp[1]])
                sA, sB = tup
                dp[key] = sA - stones[ch] + currSum, sB

            if player == "B":
                scores = [(removeStones(i, j - 1, "A", currSum - stones[j]), j),
                          (removeStones(i + 1, j, "A", currSum - stones[i]), i)]
                tup, ch = min(scores, key=lambda tp: tp[0][0] - tp[0][1] - currSum + stones[tp[1]])
                sA, sB = tup
                dp[key] = sA, sB - stones[ch] + currSum

            return dp[key]

        a, b = removeStones(0, n - 1, "A", initSum)
        return a - b


def main():
    sol = Solution()
    diff = sol.stoneGameVII([5, 3, 1, 4, 2])


if __name__ == '__main__':
    main()
