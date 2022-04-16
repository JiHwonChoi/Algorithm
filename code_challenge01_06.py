#쿼드압축?
from re import A


arr=[[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]	
answer=[]
one=0
zero=0

#배열을 4개로 나눠주는 함수
def piece(arr):
    n = len(arr)
    pieces=[]
    start=[(0,0),(0,n//2),(n//2,0),(n//2,n//2)]
    for a,b in start:
        quad=[]
        for i in range(n//2):
            row=[]
            for j in range(n//2):
                # print(a+i,b+j)
                row.append(arr[a+i][b+j])
            quad.append(row)
        pieces.append(quad)
    
    # for i in pieces:
    #     print(i)
    
    return pieces


def foo (arr):
    #필요한 변수 선언
    n = (len(arr))
    one=0
    zero=0
    
    #길이가 1인 배열이 들어오면 그냥 바로 카운트
    if(n==1):
        base=arr[0][0]
        if (base==1):
            one+=1
        else:
            zero+=1            
        return (one,zero)
    
    
    base=arr[0][0]
    bflag=0
    
    #원소가 모두 같은지 판단하기
    for i in range(n):
        for j in range(n):
            if not (base == arr[i][j]):
                bflag=1
                break;
        if(bflag):
            break
    
    #원소가 다른게 있으면 4등분해서 진행하기
    if(bflag):
        # 0...n/2-1 n/2...n-1
        pieces = piece(arr)
        for i in pieces:
            (a,b)=foo(i)
            one+=a
            zero+=b

    
    #같다면 같은거 카운트 올리기
    else:
        if (base==1):
            one+=1
        else:
            zero+=1
    return (one,zero)
            
# piece(arr)
print(foo(arr))