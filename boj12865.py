from cgi import test


maxWeight=7
itemNum=4
items=[]

itemNum , maxWeight = map(int, input().split(' '))
for i in range(itemNum):
    a,b= map(int, input().split(' '))
    items.append((a,b))

#가방안에 있는 아이템 넣는지 아닌지 기록하는 배열
# 배열 생성하기 (0,0,0,0)~(1,1,1,1)
testCase =[]
for i in range(2**itemNum):
    testCase.append("{0:b}".format(i).zfill(4))

maxValue = 0 

for i in range(len(testCase)): # 0000 - 0001 - 0010 -...-1111
    bag = 0
    value = 0
    for j in range(4): #0-1-2-3
        if int(testCase[i][j]):
            if(bag+items[j][0]<=maxWeight):
                bag += items[j][0]
                value += items[j][1]
            else: break
        if (value > maxValue): #마지막까지 확인후 최대값 비교하기
            maxValue=value
            
    print(testCase[i], bag)

print(maxValue)
            
            #리밋이 넘어가는지 확인해서 안넘어가면
                #가방에 넣구
            #넘어가면 이번 j루프는 종료하고 다음 i 루프로 넘어감
            #종료할때 이게 마지막 값이라면 맥스값과 바교한 다음에 넘어가야함 #가치 연산은 여기서 하면 됨
            
            