def solution101(participant, completion):
    #동명이인 찾아내기
    runner={}
    for x in participant:
        if(runner.get(x,0)):
            runner[x]=runner[x]+1
        else:
            runner[x]=1
            
    #완주한 사람의 수를 하나씩 걷어내기
    for x in completion:
        runner[x]=runner[x]-1
    
    #아직 값이 1인 사람 찾아내기
    for x in participant:
        if(runner[x]):
            answer=x
            break
    return answer

def solution(progresses, speeds):
    import math
    
    answer=[]
    while(len(progresses)):
        #첫번째 작업 완료하는데 얼마나 걸리나 찾기
        day = math.ceil((100-progresses[0])//speeds[0])
        cnt=1
        progresses.pop(0)
        speeds.pop(0)

        #그 뒤에 마무리 된것들 전부 빼내기
        while(len(progresses)):
            if ((progresses[0]+speeds[0]*day) >=100):
                progresses.pop(0)
                speeds.pop(0)
                cnt+=1
            else: #마무리 안된 애들은 프로그레스 더해서 업데이트하기
                for i in range(len(progresses)):
                    progresses[i]= progresses[i] + speeds[i]*day
                break
        answer.append(cnt)  
    return answer


 #문제 갯수에 맞게 답안 작성하기
 
answers=[1,2,3,4,5,1,45,1,2,3,4,5,6,7,5,4,1,2]

one =[1,2,3,4,5] 
two=[2,1,2,3,2,4,2,5]
three=[3,3,1,1,2,2,4,4,5,5]

howMany = len(answers)

#1번의 답안지 생성하기
one_answer = one*(howMany//5)
for i in range(howMany%5):
    one_answer.append(one[i])
print(one_answer)

print(three.index(max(three)))