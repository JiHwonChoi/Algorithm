<<<<<<< HEAD
=======


>>>>>>> 84b286df117af774ec8a199d06c08d3486a0f53a

maxWeight=7
itemNum=4
items=[
<<<<<<< HEAD
    # (6,13),(4,8),(3,6),(5,12)
=======
    # (6,13),
    # (4,8),
    # (3,6),
    # (5,12)
>>>>>>> 84b286df117af774ec8a199d06c08d3486a0f53a
]

itemNum , maxWeight = map(int, input().split(' '))
for i in range(itemNum):
    a,b= map(int, input().split(' '))
    items.append((a,b))

<<<<<<< HEAD
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

    

            
=======
#가방안에 있는 아이템 넣는지 아닌지 기록하는 배열
# 배열 생성하기 (0,0,0,0)~(1,1,1,1)
# testCase =[]
# for i in range(2**itemNum):
#     testCase.append("{0:b}".format(i).zfill(4))

#냅색 문제라고 함...
def Val(i,w,items):
    if(i):
        if(w >= items[i][0]):
            return max(Val(i-1,w,items), (Val(i-1,w-items[i][0],items)+items[i][1]))
        else:
            return Val(i-1,w,items)
    else:
        return 0

print(Val(itemNum-1,maxWeight,items))
   
    
#재귀함수로 풀어볼까? 재귀함수는 절대 아닌 것 같은디...

def findMax(items:list, bag, value, max, result):
    #종결조건
    if(len(items)==0):
        if(value>result):
            result=value
        return result
    
    #첫번째 아이템을 제외하고 맥스 구하기
    result = findMax(items[1:], bag, value,  max, result)
    
    bag += items[0][0]
    value += items[0][1]
    if(bag > max):
        pass
    else :
        #첫번째 아이템을 추가하고 맥스 구하기
        result = findMax(items[1:], bag, value, max, result)
        
    #result 값이 업데이트 되고 결국 이걸 리턴함
    return result

# ans = findMax(items,0, 0, maxWeight,0)
# print(ans)

# maxValue = 0 

# for i in range(len(testCase)): # 0000 - 0001 - 0010 -...-1111
#     bag = 0
#     value = 0
#     for j in range(4): #0-1-2-3
#         if int(testCase[i][j]):
#             if(bag+items[j][0]<=maxWeight):
#                 bag += items[j][0]
#                 value += items[j][1]
#             else: break
#         if (value > maxValue): #마지막까지 확인후 최대값 비교하기
#             maxValue=value
            
#     print(testCase[i], bag)

# print(maxValue)
>>>>>>> 84b286df117af774ec8a199d06c08d3486a0f53a
            
            
            