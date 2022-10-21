import unittest
from collections import defaultdict
from typing import List, Set


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(set)
        numCourseLevel: List[(int, int)] = [(0, i) for i in range(numCourses)]
        courseVisit = [False] * numCourses
        pre_reqs = [None for i in range(numCourses)]
        for pre_req, course in prerequisites:
            pre_reqs[course] = pre_req
            graph[pre_req].add(course)

        def updateLevelAndCheckCycle(pre_req_course: int, curr_level: int, visited: Set[int]) -> bool:
            if pre_req_course in visited:
                return True
            numCourseLevel[pre_req_course] = (max(numCourseLevel[pre_req_course][0], curr_level), pre_req_course)
            visited.add(pre_req_course)
            courseVisit[pre_req_course] = True;
            if pre_req_course not in graph:
                visited.remove(pre_req_course)
                return False
            for child_course in graph[pre_req_course]:
                if updateLevelAndCheckCycle(child_course, curr_level + 1, visited):
                    return True
            visited.remove(pre_req_course)

        rootExists = False
        for i in range(numCourses):
            if pre_reqs[i] is not None:
                continue
            if updateLevelAndCheckCycle(i, 0, set()):
                return []
            rootExists = True

        if not rootExists:
            return []
        if not all(courseVisit):
            return []

        numCourseLevel.sort()
        numCourseLevel.reverse()
        return [y for x, y in numCourseLevel]


class SolutionTest(unittest.TestCase):

    def setUp(self) -> None:
        self.sol = Solution()

    def test_one(self):
        n: int = 3
        preReq: List[int] = [[0, 1], [0, 2], [1, 2]]
        self.assertEqual([2, 1, 0], self.sol.findOrder(n, preReq))


if __name__ == '__main__':
    unittest.main()
