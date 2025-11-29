def solution(array, commands):
    answer = []
    
    for command in commands:
        s = command[0] - 1
        f = command[1]
        k = command[2] - 1
        
        temp = array[s:f]
        temp.sort()
        answer.append(temp[k])
        
    
    return answer