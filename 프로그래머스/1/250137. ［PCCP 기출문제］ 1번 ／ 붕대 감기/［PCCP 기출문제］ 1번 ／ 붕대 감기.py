def solution(bandage, health, attacks):
    t, x, y = bandage
    max_hp = health
    cur_hp = health

    attack_map = {time: dmg for time, dmg in attacks}
    last_time = attacks[-1][0]

    streak = 0

    for time in range(1, last_time + 1):
        if time in attack_map:
            cur_hp -= attack_map[time]
            streak = 0 
            if cur_hp <= 0:
                return -1
            continue 

        streak += 1
        cur_hp = min(max_hp, cur_hp + x)

        if streak == t:
            cur_hp = min(max_hp, cur_hp + y)
            streak = 0 
    return cur_hp
