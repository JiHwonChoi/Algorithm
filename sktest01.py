def solution(money, costs):
    answer = 0

    coin=[1,5,10,50,100,500]
    cost=[]

    for i,v in enumerate(coin):
        cost.append((i,v/costs[i]))
    cost=sorted(cost,key= lambda coin: coin[1],reverse=True)

    for i in cost:
        #가장 앞에 있는것 부터 나누기
        howmany=money//coin[i[0]]
        if(howmany):
            money=money%coin[i[0]]
            answer+=costs[i[0]]*howmany
        if(money==0):
            break

    return answer