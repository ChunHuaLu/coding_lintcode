# 2019.9.29
from collections import deque
class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: true if can finish all courses or false
    """

    def canFinish(self, numCourses, prerequisites):
        # write your code here
        edge = {i: [] for i in range(0, numCourses)}
        indegree = [0] * numCourses
        for i, j in prerequisites:
            edge[j].append(i)
            indegree[i] += 1

        course = deque([])

        for i in range(len(indegree)):
            if indegree[i] == 0:
                course.append(i)

        count = 0

        while course:
            count += 1
            root = course.popleft()
            for x in edge[root]:
                indegree[x] -= 1
                if indegree[x] == 0:
                    course.append(x)

        return count == numCourses