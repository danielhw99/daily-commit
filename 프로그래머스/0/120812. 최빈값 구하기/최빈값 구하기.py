def solution(array):
    count = {}

    for x in array:
        count[x] = count.get(x, 0) + 1

    max_count = max(count.values())
    modes = [k for k, v in count.items() if v == max_count]

    return modes[0] if len(modes) == 1 else -1