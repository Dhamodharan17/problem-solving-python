class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        #robot can move right/down
        #define moves
        
        def util(m, n):

            if m < 0 or n < 0:
                return 0

            #smallest subproblem
            if m == 0 and n == 0:
                return 1

            #left - same row and left column
            left = util(m, n-1)

            #up - same row and up column
            up = util(m-1, n)

            return left + up
        
        return util(m-1, n-1)


        
