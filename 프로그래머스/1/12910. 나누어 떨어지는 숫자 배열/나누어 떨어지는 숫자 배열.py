def solution(arr, divisor):
    answer = [element for element in arr if element%divisor==0]
    if answer == []:
        answer = [-1]
    answer.sort()
    return answer