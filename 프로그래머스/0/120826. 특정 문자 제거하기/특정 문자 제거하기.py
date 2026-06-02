def solution(my_string, letter):
    answer = ''
    
    for target_letter in my_string:
        if target_letter == letter:
            continue
        else:
            answer += target_letter
    return answer