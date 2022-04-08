from curses.ascii import isdigit


s="one4seveneight"
ans=''
three=['one', 'two', 'six']
four=['zero','four','five','nine']
five=['three','seven','eight']
i=0
number={'zero':0, 'one':1, 'two':2 , 'three':3, 'four':4 , 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
while(True):
    if(i==len(s)):
        break
    if(isdigit(s[i])):
        ans+=str(s[i])
        i+=1
    elif(s[i:i+3] in three):
        ans+=str(number[s[i:i+3]])
        i+=3
    elif(s[i:i+4] in four):
        ans+=str(number[s[i:i+4]])
        i+=4
    elif(s[i:i+5] in five):
        ans+=str(number[s[i:i+5]])
        i+=5
    else:
        print('error')
        break
print(ans)
        
        