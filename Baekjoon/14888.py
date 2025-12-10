import sys
from collections import deque
import copy

numbers, memory, queue = deque(), [], deque()
result = set()
n = int(input())

numbers.extend([int(x) for x in input().split(' ')])

plus, minus, mul, div = (int(x) for x in input().split(' '))
number = numbers.popleft()
queue.append([number, numbers.copy(), [plus, minus, mul, div]])

while queue:
    number, number_list, operator = queue.popleft()
    if len(number_list) == 0:
        result.add(number)
        continue

    temp = number_list.popleft()

    if operator[0] > 0:
        operator_temp, number_list_temp = copy.deepcopy(operator), copy.deepcopy(number_list)
        operator_temp[0] -= 1
        queue.append([number + temp, number_list_temp, operator_temp])
    if operator[1] > 0:
        operator_temp, number_list_temp = copy.deepcopy(operator), copy.deepcopy(number_list)
        operator_temp[1] -= 1
        queue.append([number - temp, number_list_temp, operator_temp])
    if operator[2] > 0:
        operator_temp, number_list_temp = copy.deepcopy(operator), copy.deepcopy(number_list)
        operator_temp[2] -= 1
        queue.append([number * temp, number_list_temp, operator_temp])
    if operator[3] > 0:
        operator_temp, number_list_temp = copy.deepcopy(operator), copy.deepcopy(number_list)
        operator_temp[3] -= 1
        if number > 0:
            queue.append([number // temp, number_list_temp, operator_temp])
        else:
            queue.append([-(abs(number) // temp), number_list_temp, operator_temp])

min_value, max_value = min(result), max(result)
print(max_value)
print(min_value)