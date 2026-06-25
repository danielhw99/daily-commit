def solution(my_string):
    answer = ''
    for letter in my_string:
        if letter.islower():
            answer += letter.upper()
        elif letter.isupper():
            answer += letter.lower()
    return answer