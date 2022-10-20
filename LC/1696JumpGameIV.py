from collections import deque


class Solution:
    def maxResult(self, nums: list[int], k: int) -> int:
        n = len(nums)
        q = deque([nums[0]], k)
        for i in range(1, min(n, k)):
            q.append(q[0] + nums[i])
            while q and q[0] < q[-1]:
                q.popleft()

        for i in range(k, n):
            nxt = q[0] + nums[i]
            if len(q) == k:
                q.popleft()
            q.append(nxt)
            while q[0] < q[-1]:
                q.popleft()
            print(q)
        return q[-1]


def main():
    sol = Solution()
    nums = [1, -5, -3, -7, 3]

    k = 3
    res = sol.maxResult(nums=nums, k=k)
    print(res)


if __name__ == '__main__':
    main()
