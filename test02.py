#오목 찾는 문제
#가로 세로 대각선 으로 m목이 되는 경우의 수를 찾아서 출력하기
# 딱 정확히 m개의 수만 있어야함. 많으면 인정안함
#대각선 탐색이 어려웠다

def solution(h, w, n, board):
    answer = 0

    #가로로 탐색 0 부터 까지 탐색한다
    for i in range(h):
        cnt=0
        for j in range(w):

            if (board[i][j]=='1'):
                cnt+=1 
            else:
                if(cnt==n):#1이 n번만 반복됐다면
                    answer+=1
                cnt=0
            if(j==w-1):#마지막 숫자일 경우
                if(cnt==n):
                    answer+=1
    print('가로:',answer)

    #세로로 탐색 
    for i in range(w):
        cnt=0
        for j in range(h):
            if (board[j][i]=='1'):
                cnt+=1
            else:
                if(cnt==n):
                    answer+=1
                cnt=0
            if (j== h-1):
                if(cnt==n):
                    answer+=1
    print('가로+세로',answer)

    #대각선 탐색
    # for i in range(h-n+1):
    #     for j in range(w-n+1):
    #         if(board[i][j]=='1'):
    #             # print('here:',i,j)
    #             cnt=1
    #             while(board[i+cnt][j+cnt]=='1'):
    #                 cnt+=1
    #                 if((i+cnt>=h or j+cnt>=w)):
    #                     break
    #             if (cnt == n):
    #                 answer+=1
    # print('아래대각선,',answer)

    #대각선 탐색
    for i in range (h-n+1):
        j=0
        cnt=0
        while(i<h and j<w):
            if(board[i][j]=='1'):
                cnt+=1
            else:
                if(cnt==n):
                    answer+=1
                cnt=0
            if(i==h-1):
                if(cnt==n):
                    answer+=1
            i+=1
            j+=1

    for j in range(1,w-n+1):
        i=0
        cnt=0
        while(i<h and j<w):
            if(board[i][j]=='1'):
                cnt+=1
            else:
                if(cnt==n):
                    answer+=1
                cnt=0
            if(i==h-1):
                if(cnt==n):
                    answer+=1
            i+=1
            j+=1

    for i in range(0,h-n+1,-1):
        j=w-1
        cnt=0
        while(i<h and j>=n-1):
            if(board[i][j]=='1'):
                cnt+=1
            else:
                if(cnt==n):
                    answer+=1
                cnt=0
            if(i==h-1):
                if(cnt==n):
                    answer+=1
            i+=1
            j-=1

    for j in range(n-1, w-2,-1):
        i=0
        cnt=0
        while(i<h and j>=0):
            if(board[i][j]=='1'):
                cnt+=1
            else:
                if(cnt==n):
                    answer+=1
                cnt=0
            if(j==0):
                if(cnt==n):
                    answer+=1
            i+=1
            j-=1
    # #위로 대각선
    # for i in range(n-1,h):
    #     for j in range (w-n+1):

    #         if (board[i][j]=='1'):
    #             cnt=1
    #             while(board[i-cnt][j+cnt]=='1'):
    #                 cnt+=1
    #                 if(i-cnt<0 or j+cnt >=w):
    #                     break
    #             print(i,j,cnt)
    #             if( cnt == n ):
    #                 answer+=1



    return answer