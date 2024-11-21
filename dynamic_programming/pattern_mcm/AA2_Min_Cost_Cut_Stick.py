class Solution(object):
    def minCost(self, n, cuts):
        
        cuts = [0] + cuts + [n]
        cuts.sort()

        def util(i, j):

            if i > j :
                return 0

            mini = float('inf')
            #j+1 since we can cut at last cut point also
            for k in range(i,j+1):
                current_cost = cuts[j+1] - cuts[i-1] + util(i,k-1) + util(k+1,j)
                mini = min(current_cost, mini)

            return mini

        #start from last array index
        return util(1,len(cuts)-2)
        

    
        
        
