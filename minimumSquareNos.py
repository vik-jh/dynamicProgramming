

import sys, math
sys.setrecursionlimit(20000000)

def minStepsTo1(n,dp):
    if n==0:
        return 0
    ans = sys.maxsize
    root = int(math.sqrt(n))
    for i in range(1,root+1):
        
        new = (n - (i**2))
        if dp[new] == -1:
            smallAns = minStepsTo1(new,dp)
            dp[new] = smallAns
            currAns = 1 + smallAns
        else:
            currAns = 1 + dp[new]
        ans = min(ans,currAns)
    return ans
    

        

    
n = int(input())


dp = [-1 for i in range(n+1)]
ans = minStepsTo1(n,dp)
print(ans)