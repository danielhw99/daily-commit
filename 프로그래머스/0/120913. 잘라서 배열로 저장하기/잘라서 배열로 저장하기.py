import math
def solution(my_str, n):
    num =  math.ceil(len(my_str)/n)
    answer = [""]*num
    cnt=0
    for i in range(num):
        for j in range(n):
            if cnt>=len(my_str): break
            answer[i] += my_str[cnt]
            cnt+=1
        
    return answer