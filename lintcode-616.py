from collections import deque
class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: the course order
    """
    def findOrder(self, numCourses, prerequisites):
        # write your code here
        if prerequisites == None:
            return []
        edges = { i:[] for i in range(0,numCourses) }
        in_node = [0]*numCourses
        for i,j in prerequisites:
            edges[j].append(i)
            in_node[i] += 1
        top_sort = deque([])
        for i in range(0,len(in_node)):
            if in_node[i] == 0:
                top_sort.append(i)
        # bfs find topology sort
        course_schedule = list()
        count = 0
        while(top_sort):
            count += 1
            root = top_sort.popleft()
            course_schedule.append(root)
            for x in edges[root]:
                in_node[x] -= 1
                if in_node[x] == 0:
                    top_sort.append(x)
        print(course_schedule)
        if count == numCourses:
            return course_schedule
        else:
            return []