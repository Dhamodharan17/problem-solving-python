#recursion
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        
       m = len(obstacleGrid)
       n = len(obstacleGrid[0])

       def util(row, col,obstacleGrid):

            if row < 0 or col < 0:
                return 0

            if row == 0 and col == 0:
                return 1

            if obstacleGrid[row][col] == 1:
                return 0

            up = util(row-1, col, obstacleGrid)
            left = util(row, col-1, obstacleGrid)

            return up + left
        
       return util(m-1, n-1, obstacleGrid)
#bottom up
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        
       rows = len(obstacleGrid)
       cols = len(obstacleGrid[0])

       dp = [[0 for _ in range(cols)] for _ in range(rows)]

       for i in range(rows):
        for j in range(cols):

            if obstacleGrid[i][j] == 1:
                continue

            if i == 0 and j == 0:
                dp[i][j] = 1
                continue

            up = 0
            left = 0
            if i > 0 and obstacleGrid[i-1][j] != 1:
                up = dp[i-1][j]
            if j > 0 and obstacleGrid[i][j-1] != 1:
                left = dp[i][j-1]
            
            dp[i][j] = up + left
            
       return dp[rows-1][cols-1]
#space
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        
       rows = len(obstacleGrid)
       cols = len(obstacleGrid[0])

       prev_row = [0] * cols

       for i in range(rows):
        current_row = [0] * cols
        for j in range(cols):

            if obstacleGrid[i][j] == 1:
                continue

            if i == 0 and j == 0:
                current_row[j] = 1
                continue

            up = 0
            left = 0
            if i > 0 and obstacleGrid[i-1][j] != 1:
                up = prev_row[j]
            if j > 0 and obstacleGrid[i][j-1] != 1:
                left = current_row[j-1]
            
            current_row[j] = up + left
        
        prev_row = current_row
            
       return prev_row[cols-1]
