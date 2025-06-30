def print_grid(grid):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(grid[i][j])
            else:
                print(str(grid[i][j]) + " ", end="")

def find_empty(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return (i, j)
    return None

def is_valid(grid, num, pos):
    row, col = pos
    
    for i in range(9):
        if grid[row][i] == num and col != i:
            return False
    
    for i in range(9):
        if grid[i][col] == num and row != i:
            return False
    
    box_x = col // 3
    box_y = row // 3
    
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if grid[i][j] == num and (i, j) != pos:
                return False
    
    return True

def solve(grid):
    find = find_empty(grid)
    if not find:
        return True
    else:
        row, col = find
    
    for i in range(1, 10):
        if is_valid(grid, i, (row, col)):
            grid[row][col] = i
            
            if solve(grid):
                return True
            
            grid[row][col] = 0
    
    return False

print("Sudoku Solver")
print("Enter the sudoku puzzle (use 0 for empty cells)")
print("Enter row by row, separated by spaces")

grid = []
for i in range(9):
    row = list(map(int, input(f"Row {i+1}: ").split()))
    grid.append(row)

print("\nOriginal Grid:")
print_grid(grid)

if solve(grid):
    print("\nSolved Grid:")
    print_grid(grid)
else:
    print("\nNo solution exists for this puzzle")

