class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:

        cuts = [0] + cuts + [n]
        cuts.sort()

        def util(i, j):

            if i > j:
                return 0

            mini  = float('inf')
            #different k cuts at each stage
            for k in range(i,j+1):
                #current_cost
                current_cut_cost = cuts[j+1] - cuts[i-1]
                #subproblem
                left_part = util(i, k-1)
                right_part = util(k+1, j)
                #total
                total_cost = current_cut_cost + left_part + right_part
                mini = min(total_cost, mini)

            return mini
            #below code
            #ignore 0 and n -> we added
        return util(1,len(cuts)-2)
