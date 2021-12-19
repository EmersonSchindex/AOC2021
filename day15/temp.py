def optimalpath(grid):
 
    # size of matrix
    (M, N) = (len(grid), len(grid[0]))
 
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
    return T[M - 1][N - 1]

def main(f): # sourcery skip: for-index-underscore  
    f = [int(item.strip()) for item in open(f, 'r').readlines()]
    grid = [[int(a) for a in str(line)] for line in f]
        
    # grid = [
    #     [4, 7, 8, 6, 4],
    #     [6, 7, 3, 9, 2],
    #     [3, 8, 1, 2, 4],
    #     [7, 1, 7, 3, 7],
    #     [2, 9, 8, 9, 3]
    # ]    
    
    size = len(grid)
    
    import time
    t = time.time()
    print(optimalpath(grid)-grid[0][0], t - time.time())

    for line in grid:
        if len(grid) == size*5:
            break
        for d in line:
            line.append(int(str(d+1)[0]))
            if len(line) == size*5:
                break

    while len(grid) < size*5:
        for i in range(size):
            grid.append(grid[ len(grid)-size ].copy())
            s = grid[-1]
            for j in range(len(s)):
                d = grid[-1][j]+1
                if d > 9:
                    d = 1
                grid[-1][j] = d

    t = time.time()
    print(optimalpath(grid)-grid[0][0], t - time.time())
    
    # 500*500 grid value check = OK
    # print(grid[6][107],   grid[33][220],  grid[17][305],  grid[10][456])
    # print(grid[106][107], grid[133][220], grid[117][305], grid[110][456])
    # print(grid[206][107], grid[233][220], grid[217][305], grid[210][456])
    # print(grid[306][107], grid[333][220], grid[317][305], grid[310][456])
    # print(grid[406][107], grid[43][220],  grid[417][305], grid[410][456])

    # import matplotlib.pyplot as plt. # Add path line later if bug not found
    # plt.imshow(grid)
    # plt.show()

if __name__ == '__main__':
    # f = 'day15test.txt'
    f = 'day15.txt'
    
    main(f)