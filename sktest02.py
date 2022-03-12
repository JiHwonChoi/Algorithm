
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
def solution(n, clockwise):
    answer = [[0]*n for _ in range(n)]

    def clockfill(start_point,clockwise): #start point가 여러개 들어와야 할 거 같음
        # diffx=next_point[0]-start_point[0]
        # diffy=next_point[1]-start_point[1]
        move=[[0,1],[1,0],[0,-1],[-1,0]]
        # y:1, x:1 , y:-1, x:-1
        # if (diffx==1):
        #     now =1
        # elif(diffy==-1):
        #     now=2
        # elif(diffx==-1):
        #     now=3
        # elif(diffy==1):
        #     now=0

        #첫 좌표 채우고
        for x in start_point:
            answer[x[0]][x[1]]=1
        #clockwise 에 따라서 bias 값 변경하기
        if(clockwise):
            bias=0
        else:
            bias=1
        val=2
        while (True):
            breakflag=0
            valflag=0
            # print('---cylce---')
            for i,x in enumerate(start_point):
                direction= (i+bias)%4
                #다음좌표 구하기
                nowX=x[0]+move[direction][0]
                nowY=x[1]+move[direction][1]
                # print(nowX,nowY)
                if(0<=nowX<n and 0<=nowY<n and answer[nowX][nowY]==0):
                    answer[nowX][nowY]=val
                    x[0]=nowX
                    x[1]=nowY
                    valflag=1
                else:
                    #주변에 빈 값이 있나 탐색하기
                    if(clockwise):
                        bias+=1
                    else:
                        bias-=1
                    break
            if(clockwise):
                if(bias>(n+1)//2):
                    break
            else:
                if(abs(bias+1)>(n+1)//2):
                    break
            if(valflag):
                val+=1


        print(answer)

    clockfill([[0,0],[0,n-1],[n-1,n-1],[n-1,0]],clockwise)
    return answer