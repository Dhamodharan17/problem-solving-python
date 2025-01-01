'''
1422. Maximum Score After Splitting a String
Solved
Easy
Topics
Companies
Hint
Given a string s of zeros and ones, return the maximum score after splitting the string into two non-empty substrings (i.e. left substring and right substring).

The score after splitting a string is the number of zeros in the left substring plus the number of ones in the right substring.

 

Example 1:

Input: s = "011101"
Output: 5 
Explanation: 
All possible ways of splitting s into two non-empty substrings are:
left = "0" and right = "11101", score = 1 + 4 = 5 
left = "01" and right = "1101", score = 1 + 3 = 4 
left = "011" and right = "101", score = 1 + 2 = 3 
left = "0111" and right = "01", score = 1 + 1 = 2 
left = "01110" and right = "1", score = 2 + 1 = 3
Example 2:

Input: s = "00111"
Output: 5
Explanation: When left = "00" and right = "111", we get the maximum score = 2 + 3 = 5
Example 3:

Input: s = "1111"
Output: 3
'''

# soln 1
class Solution:
    def maxScore(self, s: str) -> int:

        n = len(s)
        maxi = float('-inf')
        for left in range(n-1):

            zeros = 0
            for i in range(left+1):
                if s[i] == '0':
                    zeros += 1

            ones = 0
            for right in range(left+1, n):
                if s[right] == '1':
                    ones += 1

            maxi = max(zeros+ones, maxi)

        return maxi
# soln 2
class Solution:
    def maxScore(self, s: str) -> int:

        n = len(s)
        prefix_zeros = [0] * n

        for i in range(n):
            if s[i] == '0':
                prefix_zeros[i] = (prefix_zeros[i-1] + 1 )if i > 0 else 1
            else:
                prefix_zeros[i] = prefix_zeros[i-1]

        maxi = float('-inf')
        for left in range(n-1):

            zeros = prefix_zeros[left]
            ones = 0
            for right in range(left+1, n):
                if s[right] == '1':
                    ones += 1

            maxi = max(zeros+ones, maxi)

        return maxi
# soln 3
class Solution:
    def maxScore(self, s: str) -> int:

        n = len(s)
        prefix_zeros = [0] * n
        suffix_ones = [0] * n

        for i in range(n):
            if s[i] == '0':
                prefix_zeros[i] = (prefix_zeros[i-1] + 1 )if i > 0 else 1
            else:
                prefix_zeros[i] = prefix_zeros[i-1]
        
        for i in range(n-1, -1, -1):
            if s[i] == '1':
                suffix_ones[i] = (suffix_ones[i+1] +1) if i < n-1 else 1
            else:
                suffix_ones[i] = suffix_ones[i+1] if i < n-1 else 0


        maxi = float('-inf')

        for left in range(n-1):

            zeros = prefix_zeros[left]
            ones = suffix_ones[left+1]   
            maxi = max(zeros+ones, maxi)

        return maxi

#soln 4
class Solution:
    def maxScore(self, s: str) -> int:

         # since we want to zeros from left
        ones = s.count('1')
        zeros = 0
        ans = 0

        # len(s) - 1 => so we have left and right partition
        for i in range(len(s) - 1):
            # since going forward -> if encountered 1 -> 
            if s[i] == '1':
                ones -= 1
            else:
                zeros +=1
            ans = max(ans, zeros+ones)

        return ans

        

    



    
        
