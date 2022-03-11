# programmers dfsbfs 두번재 문제 풀이
def solution(n, computers):
    answer = 0
    
    #그래프와 똑같은 visited 배열 만들기
    visited = [[0]*n for _ in range(n)]
    queue =[]
    
    for x in range(n):
        for y in range(n):
            if(computers[x][y]==1 and visited[x][y]==0):
                queue=[(x,y)]
                while(queue):
                    node = queue.pop(0)
                    i = node[1]
                    for j in range(n):
                        if(computers[i][j]==1 and visited[i][j]== 0):
                            queue.append((i,j))
                            visited[i][j]=1
                answer+=1
    
    
    return answer