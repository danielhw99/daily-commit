def solution(price):
    answer = 0
    dis = 0.0
    if 500000<=price:
        dis=0.2    
    elif 300000<=price:
        dis=0.1
    elif 100000<=price:
        dis=0.05
    else: return int(price)
    
    return int(price-price*dis)