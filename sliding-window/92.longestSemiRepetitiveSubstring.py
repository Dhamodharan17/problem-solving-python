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

class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:

        left, right = 0, 1
        ans = 1
        repeated = ''
        prev = ''

        while right < len(s):
            
            #2nd adj letters - voilation case
            #already oruthan erukan, ne yaru da komali
            if repeated != '' and s[right-1] == s[right]:

                ans = max(ans, right - left)
                #by pass 1st adjacenet equal case
                while s[left] != s[left+1]:
                    left += 1
                left += 1

            #update latest repeat
            if s[right-1] == s[right]:
                repeated = s[right]

            right += 1
        
        ans = max(ans, right-left)
        return ans

        
        
