#recursion
class Solution:
    def solve(self, n, m, grid):
        
        def util(r, i, j):
            
            if j >= m or i >= m or i < 0 or j < 0:
                return float('-inf')
            
            #base case - how do you choose answer i.e based on i and j
            if r == n-1:
                
                if i == j:
                    return grid[r][j]
                else:
                    return grid[r][j] + grid[r][i]
                    
            #sub problems
            max_value = float('-inf')
            for di in range(-1, 2, 1):#person 1
                for dj in range(-1, 2, 1): #person 2
                    val = 0
                    if(i == j):
                      val =  grid[r][i] + util(r+1,di+i,dj+j)
                    else:
                      val =  grid[r][i] + grid[r][j] + util(r+1, i+di, j+dj)
                    # each step update max value since any step can be best
                    max_value = max(max_value, val)
                    
                
            return max_value    
                    
         # start from both corners   
        return util(0,0,m-1)  
# top down
class Solution:
    def solve(self, n, m, grid):
        
        dp = [ [ [ -1 for _ in range(m) ] for _ in range(m) ] for _ in range(n) ]
        
        
        def util(r, i, j):
            
            if j >= m or i >= m or i < 0 or j < 0:
                return float('-inf')
            
            if dp[r][i][j] != -1:
                return dp[r][i][j]
            
            #base case - how do you choose answer i.e based on i and j
            if r == n-1:
                
                if i == j:
                    dp[r][i][j] = grid[r][j]
                    return grid[r][j]
                else:
                    dp[r][i][j] = grid[r][j] + grid[r][i]
                    return grid[r][j] + grid[r][i]
                    
            #sub problems
            max_value = float('-inf')
            for di in range(-1, 2):#person 1
                for dj in range(-1, 2): #person 2
                    val = 0
                    if(i == j):
                      val =  grid[r][i] + util(r+1,di+i,dj+j)
                    else:
                      val =  grid[r][i] + grid[r][j] + util(r+1, i+di, j+dj)
                    # each step update max value since any step can be best
                    max_value = max(max_value, val)
                    
            dp[r][i][j] = max_value  
            return max_value    
                    
         # start from both corners   
        return util(0,0,m-1) 
#bottom up
class Solution:
    def solve(self, n, m, grid):
        
        # 3d array
        dp = [ [ [ 0 for _ in range(m) ] for _ in range(m) ] for _ in range(n) ]
        
        #base case - independent case
        for j1 in range(m):
            for j2 in range(m):
                if j1 == j2:
                    dp[n-1] [j1][j2] = grid[n-1][j1]
                else:
                    dp[n-1][j1][j2] = grid[n-1][j1] + grid[n-1][j2]
        
        #subproblem
        for i in range(n-2, -1, -1):
            for j1 in range(m):
                for j2 in range(m):
                    # now p1 in (i, j1) and p2 in (j,j2)
                    # current cost
                    if j1 == j2:
                        ans = grid[i][j1]
                    else:
                        ans = grid[i][j1] + grid[i][j2]
                        
                    # next move cost try all 9 moves
                    maxi = float('-inf')
                    for di in range(-1,2):
                        for dj in range(-1,2):
                            new_j1 = j1+di
                            new_j2 = j2+dj
                            
                            if 0<=new_j1<m and 0<=new_j2<m:
                                maxi = max(maxi,dp[i+1][new_j1][new_j2])
                                
                    dp[i][j1][j2] = maxi + ans
                    

        return dp[0][0][m-1] 
#space
class Solution:
    def solve(self, n, m, grid):
        
        # 3d array
        prev = [ [ 0 for _ in range(m) ] for _ in range(m) ]
        current = [ [ 0 for _ in range(m) ] for _ in range(m) ]
        
        #base case - independent case
        for j1 in range(m):
            for j2 in range(m):
                if j1 == j2:
                    prev[j1][j2] = grid[n-1][j1]
                else:
                    prev[j1][j2] = grid[n-1][j1] + grid[n-1][j2]
        
        #subproblem
        for i in range(n-2, -1, -1):
            for j1 in range(m):
                for j2 in range(m):
                    # now p1 in (i, j1) and p2 in (j,j2)
                    # current cost
                    if j1 == j2:
                        ans = grid[i][j1]
                    else:
                        ans = grid[i][j1] + grid[i][j2]
                        
                    # next move cost try all 9 moves
                    maxi = float('-inf')
                    for di in range(-1,2):
                        for dj in range(-1,2):
                            new_j1 = j1+di
                            new_j2 = j2+dj
                            
                            if 0<=new_j1<m and 0<=new_j2<m:
                                maxi = max(maxi,prev[new_j1][new_j2])
                                
                    #for each position of j1 and j2 with prev max moves        
                    current[j1][j2] = maxi + ans
            # update after all pairs if j1 and j2   
            prev = [row[:] for row in current]    

        return  prev[0][m-1]
