def solution(my_string):
    answer = ''
    dp = []
    for i in range(len(my_string)):
        if my_string[i] not in dp:
            dp += [my_string[i]]
            answer += my_string[i]
        else:
            continue
    return answer