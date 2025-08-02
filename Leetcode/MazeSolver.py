dirs = [
    (-1, 0),  # up
    (1, 0),   # down
    (0, -1),  # left
    (0, 1)    # right
]
def solve(maze, wall, start_char, end_char):
    start = end = None
    for y in range(len(maze)):
        for x in range(len(maze[0])):
            if maze[y][x] == start_char:
                start = (x, y)
            elif maze[y][x] == end_char:
                end = (x, y)

    if not start or not end:
        print("Start or End not found")
        return []
    seen = [[False for _ in row] for row in maze]
    path = []
    def walk(curr):
        x, y = curr
        if x < 0 or x >= len(maze[0]) or y < 0 or y >= len(maze):
            return False
        if maze[y][x] == wall or seen[y][x]:
            return False
        if (x, y) == end:
            path.append((x, y))
            return True
        seen[y][x] = True
        path.append((x, y))

        for dx, dy in dirs:
            if walk((x + dx, y + dy)):
                return True
        path.pop()
        return False
    if walk(start):
        return path
    else:
        return []
# Example usage:
maze = [
    ["#", "#", "#", "#", "E", "#"],
    ["#", " ", " ", " ", " ", "#"],
    ["#", "S", "#", "#", "#", "#"]
]

result = solve(maze, wall="#", start_char="S", end_char="E")
print("Path:", result)
