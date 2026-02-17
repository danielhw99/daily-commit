def solution(n, k):
    discount = 0
    if n>=10:
        discount = int(n/10)
        
    if discount ==0 :
        return n*12000 + k*2000
    
    return n*12000 + (k-discount)*2000
    
    