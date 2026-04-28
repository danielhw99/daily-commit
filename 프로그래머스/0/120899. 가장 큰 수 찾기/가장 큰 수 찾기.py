def solution(array):
    max_element, max_index = 0, -1
    for i in range(len(array)):
        if array[i] > max_element:
            max_element = array[i]
            max_index = i
    answer = [max_element, max_index]
    
    return answer