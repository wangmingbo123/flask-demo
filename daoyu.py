def put(hang, lie, x, y, quence: list, grid: list):
    if hang > x and x > 0 and lie > y and y > 0:
        if grid[x][y] == "1":
            quence.append((x, y))


def numIslands(grid: list) -> int:
    if grid == []:
        return 0

    num = 0
    m = len(grid)
    n = len(grid[0])

    hang = 0
    while hang < len(grid):
        # print("hang is ", hang)
        lie = 0;
        while lie < len(grid[hang]):
            # print("lie is ", lie)
            if grid[hang][lie] == "0":
                lie = lie + 1
                continue

            grid[hang][lie] = "0"
            quence = [(hang, lie)]
            while len(quence) > 0:
                zuobiao = quence.pop()
                hang = zuobiao[0]
                lie = zuobiao[1]
                put(m, n, hang - 1, lie, quence, grid)
                put(m, n, hang, lie + 1, quence, grid)
                put(m, n, hang + 1, lie, quence, grid)
                put(m, n, hang, lie - 1, quence, grid)

            num = num + 1
            lie = lie + 1

        hang = hang + 1

    return num


grid = list([
    ["1", "0", "0"],
    ["0", "1", "0"]
]
)

print(grid)

print(numIslands(grid))

# a = [(1, 2), (4, 5)]
# # print(a.pop())
# b = a.pop()
#
# print(b[0])
# print(b[1])
