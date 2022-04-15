def solution(h, w, blocks):
    answer = []

    #벽 준비하기
    wall = [[0]*w for _ in range(h)]
    # print(wall)

    #까만종이 붙이기
    for i in blocks:
        wall[i[1]][i[0]]=1
        # print(a,i[1])
    # print(wall)
    total=0
    for row in wall:
        cnt=0
        for paper in row:
            # print (paper)
            if(paper==0):
                cnt+=1
        answer.append(total+cnt)
        total+=cnt
        # print('newrow')

    return answer