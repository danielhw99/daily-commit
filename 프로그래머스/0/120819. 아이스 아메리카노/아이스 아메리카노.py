def solution(money):
    answer = [0,0]
    
    americano = 5500
    
    answer[0] = int(money / americano)
    answer[1] = money-(answer[0]*5500)
    
    return answer