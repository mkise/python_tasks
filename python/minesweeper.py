

def minesweeper(grid):
    rows = len(grid)
    cols = len(grid[0])
    result = [['' for _ in range(cols)] for _ in range(rows)]
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '-':
                count = 0
                
                # Check all 8 adjacent cells
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        new_i = i + dx
                        new_j = j + dy
                        
                        # Skip if new indices are out of bounds
                        if new_i < 0 or new_i >= rows or new_j < 0 or new_j >= cols:
                            continue
                        
                        if grid[new_i][new_j] == '#':
                            count += 1
                
                result[i][j] = str(count)
            else:
                result[i][j] = grid[i][j]
    
    return result

# Example input
input_grid = [
    ["-", "-", "-", "#", "#"],
    ["-", "#", "-", "-", "-"],
    ["-", "-", "#", "-", "-"],
    ["-", "#", "#", "-", "-"],
    ["-", "-", "-", "-", "-"]
]

# Example usage
output_grid = minesweeper(input_grid)

# Print the output grid
for row in output_grid:
    print(' '.join(row))

