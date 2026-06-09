def solution(my_string):
    answer = 0
    numbers = [int(num) for num in my_string if num.isdigit()]
    for num in numbers:
        answer += num
    
    return answer