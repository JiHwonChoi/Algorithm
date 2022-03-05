from datetime import datetime, timedelta

def solution(purchase):
    answer = [0,0,0,0,0]

    purchase_days= [datetime.strptime(x.split(' ')[0], "%Y/%m/%d") for x in purchase]
    check_days= [] #purchase days 로 부터 31일 후

    for x in purchase_days :
        date= x + timedelta(days=31)
        check_days.append(date)


    #check_days 와 purchase_days를 합쳐서 순회하기

    all_days= purchase_days+check_days

    for i,v in enumerate(all_days):
        if (i==0): #첫구매 전까지는 브론즈
            answer[0] += (v-datetime.strptime("2019/01/01", "%Y/%m/%d")).days
        else:
            for j in range(len(purchase_days)):#현재 날짜 이전까지의 구매날짜를 전부 순회
                (v-purchase_days[j]).



    return answer

#날짜가 여러개 주어지고 그 사이의 간격과 구매를 어떻게 하는지 측정하는 문제
#최근 30일간의 구매 금액에 따라 등급이 나눠짐
# 각 등급에 속해있던 일 수를 계산하시오