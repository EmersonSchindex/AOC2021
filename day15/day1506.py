from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        T = [[0] * n for _ in range(m)]
        grid[0][0] = 0

        # First left top corner cost is same.
        T[0][0] = grid[0][0]

        # First row in T
        for first_row_idx in range(1, n):
            T[0][first_row_idx] = T[0][first_row_idx-1] + grid[0][first_row_idx]

        # First col in T
        for first_col_idx in range(1, m):
            T[first_col_idx][0] = T[first_col_idx-1][0] + grid[first_col_idx][0]

        # Fill in the rest of the 2D matrix for T.
        for i in range(1, m):
            for j in range(1, n):
                T[i][j] = grid[i][j] + min(T[i-1][j], T[i][j-1])   # top/left

        # value to reach the right most end
        return T[-1][-1]


def main(f): # sourcery skip: for-index-underscore 
    f = [int(item.strip()) for item in open('input.txt', 'r').readlines()]
    grid = [[int(a) for a in str(line)] for line in f]

    import time
    t = time.time()
    s = Solution()
    print((s.minPathSum(grid)), t - time.time())

    size = len(grid)

    for line in grid:
        if len(grid) == size*5:
            break
        for d in line:
            line.append(int(str(d+1)[0]))
            if len(line) == size*5:
                break

    while len(grid) < size*5:
        for _ in range(size):
            grid.append(grid[ len(grid)-size ].copy())
            s = grid[-1]
            for j in range(len(s)):
                d = grid[-1][j]+1
                if d > 9:
                    d = 1
                grid[-1][j] = d

    s = Solution()

    print((s.minPathSum(grid)), t - time.time())

    # 500*500 grid value check = OK
#    print(grid[6][107],   grid[33][220],  grid[17][305],  grid[10][456])
#    print(grid[106][107], grid[133][220], grid[117][305], grid[110][456])
#    print(grid[206][107], grid[233][220], grid[217][305], grid[210][456])
#   print(grid[306][107], grid[333][220], grid[317][305], grid[310][456])
#    print(grid[406][107], grid[433][220],  grid[417][305], grid[410][456])

    # import matplotlib.pyplot as plt. # Add path line later if bug not found
    # plt.imshow(grid)
    # plt.show()
    
if __name__ == '__main__':
    f = 'test.txt'
    # f = 'day15.txt'
    
    main(f)