def solution(numbers):
    answer = 0
    full = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    
    for num in full:
        if num not in numbers:
            answer += num
    
    return answer