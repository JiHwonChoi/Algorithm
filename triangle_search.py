n=3
answer = []
# 채워야 할 만큼의 배열 만들기
arr=[]
for i in range(n):
    arr.append([0]*(i+1))
print(arr)
row=0
col=0
val=1
direction = [(1,0),(0,1),(-1,-1)]
d_idx=0
bflag=0

while(True):
    if(bflag):
        break
    else:
        print('input',col,row)
        arr[col][row]=val
    if(val>=len(sum(arr,[]))):
        break
    #디렉션의 다음값 확인해보고 값이 있거나, 인덱스를 넘어가면 다음 디렉션으로 진행한다
    #3번 변경한다
    for _ in range(3):
        nextc=direction[d_idx][0]+col
        nextr=direction[d_idx][1]+row
        print(nextc, nextr)
        if(0<=nextc<n and 0<=nextr<n and arr[nextc][nextr]==0):
            row=nextr
            col=nextc
            break
        else:
            d_idx = (d_idx+1)%3
            # print('change idx',_,d_idx)
            if(_ == 2):
                bflag=1
    val+=1
# print(arr)
answer= sum(arr,[])
print(answer)
