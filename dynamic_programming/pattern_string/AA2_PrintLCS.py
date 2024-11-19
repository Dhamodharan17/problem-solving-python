text1="abcde"
text2="ace"

n = len(text1)
m = len(text2)

dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

for ind1 in range(1,n+1):
    for ind2 in range(1,m+1):
        if text1[ind1-1] == text2[ind2-1]:
            dp[ind1][ind2] = 1 + dp[ind1-1][ind2-1]
        else:
            dp[ind1][ind2] = max(dp[ind1][ind2-1], dp[ind1-1][ind2])

#print lcs
lcs_string = ""
i = n
j = m
while i>0 and j>0:
    if text1[i-1] == text2[j-1]:
        lcs_string+=text1[i-1]
        i-=1
        j-=1
    elif text1[i-1]>text2[j-1]:
        i-=1
    else:
        j-=1

print(lcs_string[::-1])
