class Roatation:
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        k = k % n
        curr = count = 0
        while count < n:
            start = curr
            tmp = nums[start]
            while True:
                curr = (curr + k) % n
                tmp, nums[curr] = nums[curr], tmp
                count += 1
                if curr == start:
                    break
            curr = start + 1


def main():
    rot = Roatation()
    l = [1, 2, 3, 4, 5, 6, 7]
    rot.rotate(l, 3)
    print(l)


if __name__ == '__main__':
    main()
