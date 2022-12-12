def neigh(r, c, grid):
    res = []
    v = grid[r][c]
    if r > 0 and grid[r-1][c] <= v + 1:
        res.append((r-1, c))
    if c > 0 and grid[r][c-1] <= v + 1:
        res.append((r, c-1))
    if r < len(grid) - 1 and grid[r+1][c] <= v + 1:
        res.append((r+1, c))
    if c < len(grid[0]) - 1 and grid[r][c+1] <= v + 1:
        res.append((r, c+1))
    return res


def bfs(start, goal, grid):
    visited = [[False for x in range(len(grid[0]))]
                                        for y in range(len(grid))]
    visited[start[0]][start[1]] = True
    q = [start]
    nq = []
    steps = -1
    while len(q) > 0:
        steps += 1
        for r, c in q:
            if r == goal[0] and c == goal[1]:
                return steps
            for nr, nc in neigh(r, c, grid):
                if not visited[nr][nc]:
                    visited[nr][nc] = True
                    nq.append((nr, nc))
        q = nq
        nq = []


def main():
    with open("12.in") as f:
        grid = []
        start = None
        goal = None
        for r, line in enumerate(f.readlines()):
            row = []
            for c, char in enumerate(line.rstrip()):
                if char == 'S':
                    start = (r, c)
                    row.append(0)
                elif char == 'E':
                    goal = (r, c)
                    row.append(25)
                else:
                    row.append(ord(char) - ord('a'))
            grid.append(row)
        print("Part 1: ", bfs(start, goal, grid))

        minsteps = float('inf')
        for r, row in enumerate(grid):
            for c, val in enumerate(row):
                if val == 0:
                    steps = bfs((r, c), goal, grid)
                    if steps is not None:
                        minsteps = min(minsteps, steps)
        print("Part 2: ", minsteps)

main()
