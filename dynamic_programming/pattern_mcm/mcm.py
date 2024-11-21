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

