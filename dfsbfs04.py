def solution(tickets):
    answer = []
    
    #ticket을 뒤의 키를 사용해서 정리
    s_tickets=sorted(tickets,key= lambda x: x[1])
    
    next_visit=''
    answer.append('ICN')
    #icn 에서 출발
    for idx,i in enumerate(s_tickets):
        if(i[0]=='ICN'):
            next_visit=i[1]
            answer.append(i[1])
            s_tickets.pop(idx)
            break
    
    #다음에 방문할 곳을 찾기
    #재귀로 풀어보자
    def find_way(s_tickets,route):
        #현재 공항의 위치 route[-1]
        #더 찾아야 하는지
        if(len(route)+1==len(s_tickets)):
            return route
        #다음 공항 찾기
        # for i in s_tickets:
        #     #다음 공항이 있으면
        #     #그 공항을 route에 넣고, s_ticket에서 그 공항을 빼서 출발한다
        # #못찾으면
        # return []
        
   
    return answer


tickets=[["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
solution(tickets)