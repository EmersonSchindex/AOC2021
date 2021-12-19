def optimalpath(grid, size):
 
    # size of matrix
    (M, N) = (size, size)
 
    # `T[i][j]` maintains the minimum line to reach cell (i, j) from cell (0, 0)
    T = [[0 for x in range(N)] for y in range(M)]
    
    # fill the matrix in a bottom-up manner
    for i in range(M):
        for j in range(N):
            T[i][j] = grid[i][j]
 
            # fill the first row (there is only one way to reach any cell in the
            # first row from its adjacent left cell)
            if i == 0 and j > 0:
                T[0][j] += T[0][j - 1]
                
            # fill the first column (there is only one way to reach any cell in
            # the first column from its adjacent top cell)
            elif j == 0 and i > 0:
                T[i][0] += T[i - 1][0]
 
            # fill the rest with the matrix (there are two ways to reach any
            # cell in the rest of the matrix, from its adjacent
            # left cell or adjacent top cell)
            elif i > 0 and j > 0:
                T[i][j] += min(T[i - 1][j], T[i][j - 1])
 
    # last cell of `T[][]` stores the minimum grid to reach destination cell
    # (M-1, N-1) from source cell (0, 0)
    # First left top corner cost is same.
    
    return T[M - 1][N - 1]

def main(f): # sourcery skip: for-index-underscore  
    f = [int(item.strip()) for item in open(f, 'r').readlines()]
    grid = [[int(a) for a in str(line)] for line in f]        
    size = len(grid)
    
    import time
    t = time.time()
    print(optimalpath(grid, size), t - time.time())    

    w = len(grid[0])
    o = len(grid)
    for i in range(4):
        for line in grid:
            line.extend( [x % 9 + 1 for x in line[-w:]] )
        for line in grid[o*i:o*(i+1)]:
            grid.append( [x % 9 + 1 for x in line] )

    t = time.time()
    print(optimalpath(grid, len(grid)), t - time.time())    

if __name__ == '__main__':
    # f = 'day15test.txt'
    f = 'input.txt'
    
    main(f)