class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """

    def numIslands(self, grid):
        # write your code here
        if not grid:
            return 0

        row, column = len(grid), len(grid[0])
        cnt = 0
        for i in range(0, row):
            for j in range(0, column):
                if grid[i][j] == 1:
                    self.bfs(grid, i, j)
                    cnt += 1
        return cnt

    def bfs(self, grid, i, j):
        move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        queue = [(i, j)]
        grid[i][j] = 0
        while len(queue) > 0:
            x, y = queue.pop()
            for m_x, m_y in move:
                if 0 <= m_x + x < len(grid) and 0 <= m_y + y < len(grid[0]) and grid[m_x + x][m_y + y] == 1:
                    grid[m_x + x][m_y + y] = 0
                    queue.append((m_x + x, m_y + y))