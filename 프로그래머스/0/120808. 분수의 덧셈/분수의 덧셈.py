import math

def solution(numer1, denom1, numer2, denom2):
    denom = denom1*denom2
    numer11 = numer1*denom2
    numer22 = numer2*denom1
    numer = numer11+numer22
    
    divisor = math.gcd(denom, numer)
    denom = denom/divisor
    numer = numer/divisor
    
    answer = [numer,denom]
    return answer