grid =  [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

def char_grid():
    grid_T = list(zip(*grid))
    reversed_ = [[grid[j][i] for j in range(len(grid))] for i in range(len(grid[0]))]    
    for i in range(6):
        for j in range(9):
            print(reversed_[i][j], end = ' ')
        print("\n")

if __name__ == "__main__":
    char_grid()