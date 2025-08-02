dirs = [(0, -2), (2, 0), (0, 2), (-2, 0)]  # left, down, right, up

def funcHopSkipJump(matrix):
    start = (1, 1)
    seen = [[False for _ in row] for row in matrix]
    path = []

    def skip(x, y):
        if y < 0 or y >= len(matrix) or x < 0 or x >= len(matrix[0]):
            return False
        if seen[y][x]:
            return False

        seen[y][x] = True
        path.append((x, y))

        moved = False
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= ny < len(matrix) and 0 <= nx < len(matrix[0]) and not seen[ny][nx]:
                if skip(nx, ny):
                    moved = True

        if not moved:
            return True

        path.pop()
        return False

    skip(*start)
    return path

def main():
    matrix = [
        [3, 4, 5],
        [2, 90, 6],
        [7, 6, 4]
    ]
    result = funcHopSkipJump(matrix)
    if result:
        x, y = result[-1]
        print(matrix[y][x])
    else:
        print("No move made")

if __name__ == "__main__":
    main()
