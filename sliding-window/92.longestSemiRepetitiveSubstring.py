class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        
        ans,n =0, len(s)

        for i in range(n):
            semi_rep = False
            
            for j in range(i,n):

                if j == n-1:
                    ans = max(ans, j-i+1)
                    break

                if s[j] == s[j+1] and semi_rep == True:
                    ans = max(ans, j-i+1)
                    break

                elif s[j] == s[j+1]  and semi_rep == False:
                    semi_rep = True
                    ans = max(ans, j-i+1)
                    
                else:
                    ans = max(ans, j-i+1)

        return ans
        
