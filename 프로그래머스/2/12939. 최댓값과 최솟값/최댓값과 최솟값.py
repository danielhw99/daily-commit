def solution(s):
    answer = s.split()
    li =[]
    for item in answer:
        num = int(item)
        li.append(num)
    real_answer = ''
    real_answer += str(min(li))
    real_answer += ' '
    real_answer += str(max(li))
    return real_answer