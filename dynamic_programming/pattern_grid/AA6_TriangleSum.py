class Solution(object):
    def minimumTotal(self, triangle):
        
        rows =  len(triangle)
        
        def util(m, n):
            
            if m >= rows:
                return float('inf')
            
            if m+1 == rows:
                return triangle[m][n]

            next = util(m+1, n)
            nextX = util(m+1,n+1)

            return triangle[m][n] + min(next, nextX)
        
        return util(0,0)
#space
class Solution(object):
    def minimumTotal(self, triangle):
        
        rows =  len(triangle)
        # we need just next and next+1 of prev row
        prev_row = [0] * rows

        for i in range(rows):
            prev_row[i] = triangle[rows-1][i]
        
        for i in range(rows-2,-1,-1):
            current_row = [0] * rows
            for j in range(i,-1,-1):
                next = prev_row[j]
                nextX = prev_row[j+1]
                current_row[j] = min(next, nextX) + triangle[i][j]
            prev_row = current_row
            
        return prev_row[0]
       
