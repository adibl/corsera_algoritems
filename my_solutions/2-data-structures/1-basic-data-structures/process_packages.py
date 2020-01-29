from collections import deque
q = deque()
buffer_size, number_of_packeges = input().split()
number_of_packeges = int(number_of_packeges)
buffer_size = int(buffer_size)
if buffer_size == 0:
    pass
time = 0
next_time, next_length = [int(x) for x in input().split()]
number_of_packeges -= 1
print_arr = []
while len(q) != 0 or number_of_packeges != 0:
    if len(q) > 0 and q[0] == -1:
        print_arr.append(-1)
        q.popleft()
    elif len(q) == 0 or time + q[0] > next_time:
        if len(q) + 1 <= buffer_size:
            q.append(next_length)
        else:
            q.append(-1)
        if number_of_packeges > 0:
            next_time, next_length = [int(x) for x in input().split()]
            number_of_packeges -= 1
        else:
            next_time = float('inf')
            next_length = -2
    elif len(q) > 0:
        print_arr.append(time)
        time += q.popleft()
    else:
        time = next_time
while len(q) > 0:
    print_arr.append(time)
    time += q.popleft()
if next_length != -2:
    print_arr.append(time)

for var in print_arr:
    print(var)




