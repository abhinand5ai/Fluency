class Solution:
    def findLengthOfShortestSubarray(self, arr: list[int]) -> int:
        n = len(arr)
        if n < 2:
            return 0
        left = 0
        right = n - 1

        while left < n - 1 and arr[left] <= arr[left + 1]:
            left += 1

        if left == n - 1:
            return 0

        while right > 0 and arr[right - 1] <= arr[right]:
            right -= 1

        mn = min(n - left - 1, right)
        i = 0
        j = right
        while i <= left and j < n:
            if arr[i] <= arr[j]:
                # print(i,j)
                mn = min(mn, j - i - 1)
                i += 1
            else:
                j += 1

        return mn
