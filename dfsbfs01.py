#프로그래머스 dfs/bfs 01번 문제 풀이
# dp로 접근했다

def solution(numbers, target):
    answer = 0
    
    dp= [[-1]*(2*sum(numbers)) for _ in range(len(numbers)+1)]
    bias = sum(numbers) - target
    print(dp)
    i = len(numbers)
    
    
    #구하고자 하는것 dp[len(numbers)][target+bias]
    #find 에 numbers 들어가는게 아니고... len(number)이 들어가도록 해야함
    def find(i,target):
        number_now= numbers[i-1]
        target_plus=target+number_now
        target_minus=target-number_now
        
        print(i, target)
        
        if(dp[i][target] != -1):
            return dp[len(numbers)][target]
        else:
            if(i==1):
                if((target_plus==bias or target_minus==bias)):
                    # print('return 1')
                    return 1
                else:
                    # print('return 0')
                    return 0
            else:
                val = find(i-1,target_minus) + find(i-1, target_plus)
                print('now on',i,target,':',val)
                return val
            
    answer= find(i, target+bias)
                    
        
    
    return answer

print('this is',solution([1,1,1,1,1],3))