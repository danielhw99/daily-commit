def solution(my_string):
    answer = ''
    check = ["a","e","i","o","u"]
    for char in my_string:
        if char in check:
            continue
        answer += char
    return answer