#reucrsion
class Solution(object):
    def minFallingPathSum(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])

        def util(m, n):

            if n < 0 or n >= cols:
                return float('inf')
            
            if m==0:
                return matrix[m][n]

            up = util(m-1,n)
            next = util(m-1, n+1)
            nextX = util(m-1, n-1)

            return min(min(next, nextX),up) + matrix[m][n]
        
        min_cost = float('inf')
        for i in range(rows):
            val = util(rows-1,i)
            min_cost = min(val, min_cost)
        return min_cost

      #top down
      class Solution(object):
    def minFallingPathSum(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])

        dp = [[0 for _ in range(rows)] for _ in range(cols)]

        for i in range(rows):
            dp[0][i] = matrix[0][i]
        
        for i in range(1,rows):
            for j in range(0,rows):

                up = dp[i-1][j]

                next = float('inf')
                if j > 0:
                    next = dp[i-1][j-1]

                nextX = float('inf')
                if j < rows-1:
                    nextX = dp[i-1][j+1]

                dp[i][j] = min(up,min(next, nextX))+ matrix[i][j]
        
        return min(dp[rows-1])

#space
class Solution(object):
    def minFallingPathSum(self, matrix):
        rows = len(matrix)

        prev_row = [0] * rows    

        for i in range(rows):
            prev_row[i] = matrix[0][i]
        
        for i in range(1,rows):
            current_row = [0] * rows
            for j in range(0,rows):

                up = prev_row[j]

                next = float('inf')
                if j > 0:
                    next = prev_row[j-1]

                nextX = float('inf')
                if j < rows-1:
                    nextX = prev_row[j+1]

                current_row[j] = min(up,min(next, nextX))+ matrix[i][j]

            prev_row = current_row
        
        return min(prev_row)

        
