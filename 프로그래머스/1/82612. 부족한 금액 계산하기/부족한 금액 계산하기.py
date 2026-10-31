def solution(price, money, count):
    currprice=price
    sum=0
    for i in range(1, count+1):
        currprice=i*price
        sum+=currprice
    return sum-money if sum>money else 0