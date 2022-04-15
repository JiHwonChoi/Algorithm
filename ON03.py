def solution(wolf_count, sheep_count, cabbage_count, wolf_weight, sheep_weight, cabbage_weight, limit):
    answer = 0

    here=[wolf_count, sheep_count, cabbage_count]
    there=[0,0,0]
    weight=[wolf_weight, sheep_weight, cabbage_weight]
    boat=[]
    for i in range(3):
        boat.append(limit//weight[i])

    #here 에 있는 모든 것의 무게 제한이 뗏목의 무게 제한보다 작을 경우
    def carry(here,there,weight,limit):
        tot=0
        for i in range(3):
            tot+=here[i]*weight[i]
        if(tot<=limit):
            return 1
        else:
            return -1

    #here이고 there 이고 0 > 1 > 2 되어야 함
    # 늑대를 옮길 수 있으면 늑대를 옮긴다: (there의 양 - 보트의 맥시멈 양의 수 ) 만큼 옮긴다
    # 늑대를 옮길 수 없으면 양을 옮긴다: there의 
    # 양을 옮길 수 없으면 양배추를 옮긴다
    # while (True):
    #     break_flag=0
    #     for i in range(3):
    #         if (here[i]==0):
    #             break_flag+=1
    #     if(break_flag==3):
    #         break

    #     if(here[0]<here[1]):
    #         if(here[1]<here[2]):#늑<양<추 =늑먼저 옮기기
    #             pass
    #         else:#양>추 =양먼저 옮기기
    #             if(here[1]-boat[1]<here[2]):#양을 배애 태우면 만족하는 경우  
    #                 pass
    #             elif(here[2]<=boat[2]): #양배추 싹 실어서 나를 수 있는 경우
    #                 pass

    answer= carry(here,there,weight,limit)
    # print(here)

    return answer