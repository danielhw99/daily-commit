def solution(rsp):
    answer = ''
    lenOfRSP = len(rsp)
    for i in range(lenOfRSP):
        if rsp[i] == '2':
            answer += '0'
        elif rsp[i] == '0':
            answer += '5'
        else:
            answer += '2'
    return answer