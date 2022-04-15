

def solution(room):
    answer = 0
    height = len(room)
    width = len(room[0])
    #세로로 탐색을 하는데
    flag=0
    for col in range(width):
        for row in range(height-1):#바닥 직전까지만 살펴본다
            now = room[row][col]
            below = room[row+1][col]
            #다음이 바닥이 아닌데 먼지 만나면 플래그 켜짐 ->  청소 숫자 올라감
            if (not below=='#') and (now =='$'):
                flag=1
                answer+=1
            if (below =='#') and ((now=='$') or (flag==1)):
                flag=0
                answer+=1
            #다음이 바닥인데 ( 현재 먼지가 있다 or 플래그 켜져있다) -> 청소하고 플래그 꺼짐


    return answer