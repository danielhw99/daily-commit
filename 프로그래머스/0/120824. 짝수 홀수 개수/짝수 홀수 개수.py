def solution(num_list):
    answer = []
    odd, even = 0, 0
    for item in num_list:
        if item%2==0:
            even+=1
        else:
            odd+=1
    answer = [even, odd]
    return answer