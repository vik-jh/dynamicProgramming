
from sys import stdin

def lcs(str1, str2) :
    n = len(str1)
    m = len(str2)
    dp = [[0 for j in range(m+1)]for i in range(n+1)]
    
    for i in range(n-1, -1, -1):
        for j in range(m-1, -1, -1):
            if str1[i] == str2[j]:
                dp[i][j] = 1 + dp[i+1][j+1]
                
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j+1])
                
    return dp[0][0]
	#Your code goes here

  


#main
s = str(stdin.readline().rstrip())
t = str(stdin.readline().rstrip())

print(lcs(s, t))
