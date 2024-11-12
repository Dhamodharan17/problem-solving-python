#top down
class Solution(object):
    def minPathSum(self, grid):
        
        m = len(grid)
        n = len(grid[0])
        dp = [[-1 for _ in range(n)] for _ in range(m)]

        def util(row, col):

            if row < 0 or col < 0:
                return float('inf')

            if row == 0 and col == 0:
                return grid[row][col]
            
            if dp[row][col] != -1:
                return dp[row][col]
        
            up = util(row-1,col)
            left = util(row, col-1)

            dp[row][col] = min(up, left) + grid[row][col]
            
            return dp[row][col]
            
        return util(m-1, n-1)

#bottom up
class Solution(object):
    def minPathSum(self, grid):
        
        m = len(grid)
        n = len(grid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j] = grid[i][j]
                    continue
                up = float('inf')
                left = float('inf')
                if i > 0 :
                    up =  dp[i-1][j]
                if j >0 :
                    left = dp[i][j-1]

                dp[i][j] = grid[i][j] + min(up,left)

        return dp[m-1][n-1]
  # space
  class Solution(object):
    def minPathSum(self, grid):
        
        m = len(grid)
        n = len(grid[0])
        
        prev = [0] * n
        
        for i in range(m):
            current = [0] * n
            for j in range(n):
                if i == 0 and j == 0:
                    current[j] = grid[i][j]
                    continue
                up = float('inf')
                left = float('inf')
                if i > 0 :
                    # same col, up value
                    up =  prev[j]
                if j >0 :
                    # left of same row
                    left = current[j-1]

                current[j] = grid[i][j] + min(up,left)

            prev = current

        return prev[n-1]
