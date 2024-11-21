#top down
class Solution:
  #current_cost - changes based on problem
    def matrixMultiplication(self, arr):
        
        n = len(arr)
        
        def util(i,j):
            
            # number of operation to multiply single matrix
            if i == j:
                return 0
                
            mini = float('inf')
            for k in range(i, j):
                #(AX)(BCD)
                current_cost = arr[i-1] * arr[k] * arr[j] # to mutiply AX and BCD
                left_cut = util(i, k) # to multiply AX
                right_cut = util(k+1, j) # to multiply BCD
                mini = min(mini, left_cut + current_cost + right_cut) #total
                
            return mini
            
                
        return util(1, n-1) 

#bottom up
class Solution:
    def matrixMultiplication(self, arr):
        
        n = len(arr)
        dp = [[0] * n for _ in range(n)]
        
        for i in range(n):
            dp[i][i] = 0
        #cuts start from end
        for i in range(n-2,0,-1):
            for j in range(i+1, n):
                mini = float('inf')
                for k in range(i,j):
                    steps = (arr[i-1] * arr[k] * arr[j]
                    + dp[i][k]
                    + dp[k+1][j])
                    mini = min(mini, steps)
                dp[i][j] = mini
        
        return dp[1][n-1]
