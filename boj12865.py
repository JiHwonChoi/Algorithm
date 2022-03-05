
maxWeight=7
itemNum=4
items=[
    # (6,13),(4,8),(3,6),(5,12)
]

itemNum , maxWeight = map(int, input().split(' '))
for i in range(itemNum):
    a,b= map(int, input().split(' '))
    items.append((a,b))

dp = [[0 for _ in range(maxWeight+1)]for _ in range(itemNum+1)]
for i in range(itemNum+1):
    for j in range(maxWeight+1):
        if(i and j):
            if(j-items[i-1][0]>=0):
                dp[i][j]= max(dp[i-1][j],(dp[i-1][j-items[i-1][0]]+items[i-1][1]))#여기가 문제 dp[j-items[i][0]] 인덱스가 나가버린다
            else:
                dp[i][j]=dp[i-1][j]
        elif (i==0 or j==0):
            dp[i][j]=0
        # elif (i==0):
        #     dp[i][j]= 0
        # elif (j==0):
        #     dp[i][j]=dp[i-1][j]
print(dp[itemNum][maxWeight])

    

            
            
            
            