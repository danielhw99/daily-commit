def solution(score):
    averages = [sum(s) / len(s) for s in score]
    sorted_averages = sorted(averages, reverse=True)
    answer = [sorted_averages.index(avg) + 1 for avg in averages]
    return answer