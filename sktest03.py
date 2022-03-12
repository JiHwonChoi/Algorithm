def solution(width, height, diagonals):
    answer = 0

    #최단거리
    minimum = width+height+1

    ways=[[0]*(width+1) for _ in range(height+1)]

    def route(x,y):#0,0 에서 x,y로 가는 최단경로

        if(x==0 or y==0):
            ways[x][y]=1
        if(ways[x][y]):
            return ways[x][y]
        else:
            ways[x][y]=route(x-1,y)+route(x,y-1)
            return ways[x][y]

    for x in diagonals:
        #대각선의 좌표 구하기
        #x(n,m)
        a=[width-x[0],height-x[1]+1]
        b=[width-x[0]+1, height-x[1]]
        #0,0~a * b~width,height
        #0,0~b * a~width,height
        route_0a=route(a[0],a[1])
        route_bn=route(width-b[0],height-b[1])
        answer+=route_0a*route_bn

        route_0b=route(b[0],b[1])
        route_an=route(width-a[0],height-a[1])
        answer+=route_0b*route_an
    answer=answer%10000019



    return answer