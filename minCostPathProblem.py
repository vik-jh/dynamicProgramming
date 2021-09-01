
import sys
def cost(li,i,j,m,n,dp):
    if i>=m or j>=n:
        return sys.maxsize
    if i==m-1 and j==n-1:
        return li[i][j]
    if dp[i][j]!=-1:
        ans1=dp[i+1][j]
        ans2=dp[i][j+1]
        ans3=dp[i+1][j+1]
    else:
        
        ans1=cost(li,i+1,j,m,n,dp)
        dp[i+1][j]=ans1
        ans2=cost(li,i,j+1,m,n,dp)
        dp[i][j+1]=ans2
        ans3=cost(li,i+1,j+1,m,n,dp)
        dp[i+1][j+1]=ans3
        
    ans=li[i][j]+min(ans1,ans2,ans3)
      
    return ans
sys.setrecursionlimit(100000)
str=input().split()
m,n=int(str[0]),int(str[1])
li=[[int(j) for j in input().split()] for i in range(m)]
dp=[[-1 for j in range(n+1)]for i in range(m+1)]
print(cost(li,0,0,m,n,dp))
