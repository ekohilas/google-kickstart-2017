def check_grid(grid, height, width, k=1):
    tree_heights = {}
    for r in range(height):
        for c in range(width):
            tree_height(tree_heights, grid, height, width, r, c)
    #return max([max(d.values()) for d in tree_heights.values()])**2
    return max(tree_heights.values())**2

def tree_height(d, grid, height, width, x, y):

    if x >= height or x < 0 or y >= width or y < 0 or grid[x][y] == False:
        d[(x, y)] = 0

    elif (x, y) not in d:
        left   = tree_height(d, grid, height, width, x+1, y-1)
        middle = tree_height(d, grid, height, width, x+1, y  )
        right  = tree_height(d, grid, height, width, x+1, y+1)

        if middle:
            d[(x, y)] = middle + 1
        if left and middle and right:
            d[(x, y)] = min(left, middle, right) + 1
        elif grid[x][y] == True:
            d[(x, y)] = 1

    return d[(x, y)]

def check_tree(grid, row, col, h=1):
    line_size = count_row(grid, row, col, h)
    if line_size:
        return check_tree(grid, row, col, h+1) + line_size
    else:
        return 0

def count_row(grid, r, c, h):
    #print(c-h+1, c+h)
    for i in range(c-h+1, c+h):
        if i < 0 or i >= len(grid[0]) or r+h-1 >= len(grid) or grid[r+h-1][i] == False:
            return 0
    return 2*(h-1)+1

def print_cases(func):
    for i in range(1, int(input())+1):
        height, width, k = map(int, input().split())
        grid = []
        for _ in range(height):
            grid.append([True if x == "#" else False for x in input()])
        output = func(grid, height, width, k)
        print("Case #{}: {}".format(i, output))

if __name__ == "__main__":
    print_cases(check_grid)

