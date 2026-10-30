def getYaksu(num):
    data = []
    for i in range(1,num+1):
        if num%i==0:
            data.append(i)
    return data

def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        data=getYaksu(i)
        if len(data)%2==0:#짝수
            answer+=i
        elif len(data)%2==1:#홀수
            answer-=i
    return answer