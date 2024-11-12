#top down
class Solution(object):
    def uniquePaths(self, m, n):
        
        dp = [[-1 for _ in range(n)] for _ in range(m)]

        def util(row, col, m, n):

            if row < 0 or col < 0:
                return 0

            if row == 0 and col == 0:
                return 1

            if dp[row][col] != -1:
                return dp[row][col]
                
            up = util(row-1, col, m, n)
            left = util(row, col-1, m, n)

            dp[row][col] = up + left

            return dp[row][col]

        return util(m-1,n-1,m,n)
#Bottom Up
class Solution(object):
    def uniquePaths(self, m, n):
        
        dp = [[0 for _ in range(n)] for _ in range(m)]
    
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j] = 1
                    continue
                if i > 0:
                    dp[i][j] += dp[i-1][j]
                if j > 0:
                    dp[i][j] += dp[i][j-1]

        return dp[m-1][n-1]

       
  
