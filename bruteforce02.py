import time

numbers="123"
def find_num(start,numbers,answer:list,maxLen):
    # print(start, numbers, answer)
    for idx, i in enumerate(numbers):
        start2 = start+i
        numbers2=numbers
        if(int(start2) not in answer):
            answer.append(int(start2))
        numbers2=numbers2[:idx]+numbers2[idx+1:]
        if(numbers2 and len(start)<maxLen):
            find_num(start2,numbers2,answer,maxLen)
    return answer
# start_time=time.time()      
ans = find_num("",numbers,[],len(numbers))
print(ans)
# print("time :", time.time() - start_time) 

# sosu=[]
# for i in ans:
#     if(i==2):
#         sosu.append(i)
#     else:
#         for j in range(2,i):
#             if not j==i-1 and i%j==0:
#                 break;
#             if j==i-1 and not i%j==0 :
#                 sosu.append(i)
# print(sosu)

# #프로그래머스 해설
# def getAllCombination(numbers, numList, leftCipher):
#     '''
#     numbers : 총 숫자카드 list
#     numList : 가능한 숫자 배열 list
#     leftCipher : 남은 자릿수
#     '''

#     # 현재 가능한 숫자 배열 list를 기준으로 추가가 가능한 숫자들은 찾는다. 
#     newNumList = [[]]
#     for li in numList:
#         for i in numbers:
#             if i in li and li.count(i) <= numbers.count(i) - 1:
#                 tmp = li[:]
#                 tmp.append(i)
#                 newNumList.append(tmp)
#             if i not in li:
#                 tmp = li[:]#tmp 에 복사 하기
#                 tmp.append(i)
#                 newNumList.append(tmp)

#     leftCipher -= 1

#     if leftCipher == 0:
#         return newNumList
#     else:
#         return getAllCombination(numbers, newNumList, leftCipher)
            

# availableAnswer = getAllCombination(numbers, [[]], len(numbers))

from itertools import permutations
numbers="123"
for i in range(len(numbers)+1):
    print(list(map(''.join,permutations(numbers,i))))
