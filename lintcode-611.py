from collections import deque


class Solution:
    """
    @param grid: a chessboard included 0 (false) and 1 (true)
    @param source: a point
    @param destination: a point
    @return: the shortest path
    """

    def shortestPath(self, grid, source, destination):
        # write your code here
        knight_path = deque([])
        knight_path.append([source.x, source.y, 0])
        knight_visited = set()
        knight_visited.add((source))
        len_x = len(grid)
        len_y = len(grid[0])
        if not source or not destination:
            return -1
        if source == destination:
            return 1
        # print(source.x,source.y)
        dest_f = 0
        while knight_path and dest_f == 0:
            knight_walk = [[1, 2], [1, -2], [-1, 2], [-1, -2], [2, 1], [2, -1], [-2, 1], [-2, -1]]
            curr_pos_x, curr_pos_y, length = knight_path.popleft()
            if curr_pos_x == destination.x and curr_pos_y == destination.y:
                print(knight_visited)
                return length
            for x, y in knight_walk:
                tmp_x = curr_pos_x + x
                tmp_y = curr_pos_y + y
                # print(tmp_x,tmp_y)
                if tmp_x < len_x and tmp_x >= 0 and tmp_y < len_y and tmp_y >= 0:
                    if grid[tmp_x][tmp_y] != 1 and (tmp_x, tmp_y) not in knight_visited:
                        # print(tmp_x,tmp_y)
                        knight_path.append([tmp_x, tmp_y, length + 1])
                        knight_visited.add((tmp_x, tmp_y))
        return -1
