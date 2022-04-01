brown =8
yellow = 1
answer=[]

for i in range(yellow,0,-1):
    if (yellow%i==0):
        m=i
        n=yellow//i
        if(brown == (m+n+2)*2):
            answer.append(m+2)
            answer.append(n+2)
            break;
print(answer)
    