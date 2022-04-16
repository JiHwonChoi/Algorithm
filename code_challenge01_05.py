# count 메소드를 활용해서 풀어보자

s='110010101001'
answer=[]
num=0
cnt=0
zero=0

while (not (s=='1')):
    ones = s.count('1')
    zero += len(s)-ones
    s=bin(ones)[2:]
    cnt+=1

# while(True):
    
#     if(s=='1'):
#         break
#     #0 걷어내기
#     new_s=''
    
#     for i in s:
#         if (i=='1'):
#             new_s+=i
#         else:
#             zero+=1
            
#     c=len(new_s)
#     s=bin(c)[2:]
    
#     # print('new',s,new_s)
#     cnt+=1
#     if(cnt>10):
#         break
    
answer.append(cnt)
answer.append(zero)
print(answer)