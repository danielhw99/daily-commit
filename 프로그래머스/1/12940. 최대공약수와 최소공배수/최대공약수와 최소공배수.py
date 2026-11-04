import math
def solution(n, m):
    # 최대공약수 (GCD)
    gcd_val = math.gcd(n, m)

    # 최소공배수 (LCM)
    lcm_val = math.lcm(n, m)
    
    return [gcd_val,lcm_val]