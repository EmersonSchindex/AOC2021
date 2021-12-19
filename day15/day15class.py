from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        T = [[0] * n for _ in range(m)]

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
    f = [int(item.strip()) for item in open(f, 'r').readlines()]
    grid = [[int(a) for a in str(line)] for line in f]

    import time
    t = time.time()
    s = Solution()
    print(s.minPathSum(grid), t - time.time())

    w = len(grid[0])
    o = len(grid)
    for i in range(4):
        for line in grid:
            line.extend( [x % 9 + 1 for x in line[-w:]] )
        for line in grid[o*i:o*(i+1)]:
            grid.append( [x % 9 + 1 for x in line] )

    s = Solution()
    t = time.time()
    print(s.minPathSum(grid), t - time.time())

if __name__ == '__main__':
    # f = 'day15test.txt'
    f = 'input.txt'
    
    main(f)