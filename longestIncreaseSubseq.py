from sys import stdin

'''def lis(arr, i, n): 
    n = len(arr)
    if i == n: 
        return 0
    count = 1
        
   
    
    for i in range(n):
        if arr[i] > arr[i+1]:
            count = count + 1
            
    return count

            
            '''
def lis(arr): 
    n = len(arr)  
    lis = [1]*n 

    for i in range (1 , n): 
        for j in range(0 , i): 
            if arr[i] > arr[j] and lis[i]< lis[j] + 1 : 
                lis[i] = lis[j]+1
    maximum = 0
    for i in range(n): 
        
        maximum = max(maximum , lis[i])
        
    return maximum 




n = int(input())
li = [int(ele) for ele in input().split()]
print(lis(li))



        

