#recursion
class Solution(object):
    def calculateMinimumHP(self, dungeon):
        
        rows = len(dungeon)
        cols = len(dungeon[0])
        def util(m, n):

            if m >= rows or n >= cols:
                return float('inf')

            if m == rows-1 and n == cols-1:
                return max(1, 1-dungeon[m][n])
            
            down = util(m+1,n)
            right = util(m,n+1)

            miniEnergyForNextCell = min(right,down)

            return max(1,miniEnergyForNextCell - dungeon[m][n])
    
        return util(0, 0)
#bottom up
class Solution(object):
    def calculateMinimumHP(self, dungeon):
        
        rows = len(dungeon)
        cols = len(dungeon[0])

        dp = [[float('inf') for _ in range(cols+1)] for _ in range(rows+1)]
        #addind right and down for last cell
        dp[rows-1][cols] = 1
        dp[rows][cols-1] = 1
        
        for i in range(rows-1,-1,-1):
            for j in range(cols-1,-1,-1):
                down = dp[i+1][j]
                right = dp[i][j+1]
                min_energy = min(down,right)
                dp[i][j] = max(1,min_energy - dungeon[i][j])

        return dp[0][0]
   
