def solution(begin, target, words):
    answer = 0
    def cnt_dif(word1, word2):
        cnt=0
        for i,x in enumerate(word1):
            if(x!=word2[i]):
                cnt+=1
        return cnt
    
    #target 이 words 안에 있는지 확인
    if (target not in words):
        return 0
    stack=[]
    depth=0
    
    for y in words:
        if (cnt_dif(begin,y)==1):
            stack.append(y)
    if(stack):
        depth+=1
        
    while (stack):
        depth+=1
        list1=stack.copy()
        stack=[]
        for x in list1:
            words.remove(x)
            for y in words:
                if(cnt_dif(x,y)==1):
                    if(y==target):
                        return depth
                    else:
                        stack.append(y)
        print(depth, stack, words)
    
    
    return 0

a=solution("hit","cog",["hot","dot", "dog", "lot", "log", "cog"])
print(a)