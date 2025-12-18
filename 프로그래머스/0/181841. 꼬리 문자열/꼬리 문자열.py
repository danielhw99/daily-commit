def solution(str_list, ex):
    answer = ''
    for part in str_list:
        if ex in part:
            continue
        else:
            answer += part
    return answer