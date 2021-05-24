grid = []
for grid_i in range(20):
    grid_t = [int(grid_temp) for grid_temp in input().strip().split(' ')]
    grid.append(grid_t)

prod = []
for i in range(20):
    for j in range(20):
        if i <= 16:
            prod.append(grid[i][j] * grid[i + 1][j] * grid[i + 2][j] * grid[i + 3][j])
            if j <= 16:
                prod.append(grid[i][j] * grid[i + 1][j + 1] * grid[i + 2][j + 2] * grid[i + 3][j + 3])
            else:
                pass

            if j >= 3:
                prod.append(grid[i][j] * grid[i + 1][j - 1] * grid[i + 2][j - 2] * grid[i + 3][j - 3])
            else:
                pass
        else:
            pass
        if j <= 16:
            prod.append(grid[i][j] * grid[i][j + 1] * grid[i][j + 2] * grid[i][j + 3])
        else:
            pass

print(max(prod))
