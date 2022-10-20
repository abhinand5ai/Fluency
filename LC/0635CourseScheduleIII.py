from functools import cache
import heapq


class Solution:
    def scheduleCourse(self, courses: list[list[int]]) -> int:
        courses.sort(key=lambda x: x[1])
        hp = []
        currTime = 0
        for duration, endTime in courses:
            if currTime + duration <= endTime:
                heapq.heappush(hp, -1 * duration)
                currTime += duration
            else:
                if hp and -1 * hp[0] > duration:
                    neg_ex = heapq.heappop(hp)
                    heapq.heappush(hp, -1 * duration)
                    currTime += duration + neg_ex

        return len(hp)


def main():
    sol = Solution()
    mx = sol.scheduleCourse([[5, 5], [4, 6], [2, 6]])
    print(mx)


if __name__ == '__main__':
    main()
