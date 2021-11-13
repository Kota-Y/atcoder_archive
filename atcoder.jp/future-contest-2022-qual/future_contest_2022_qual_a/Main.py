import sys
from collections import deque

n, m, k, r = list(map(int, input().split()))
task_difficulty = []
for i in range(n):
    task_difficulty.append(list(map(int, input().split())))
task_dependency = [[] for _ in range(n)]
task_dependency_tmp = [[] for _ in range(n)]
for i in range(r):
    temp = list(map(int, input().split()))
    task_dependency[temp[1] - 1].append(temp[0] - 1)
    task_dependency_tmp[temp[0] - 1].append(temp[1] - 1)
# -1: not started
#  0: started
#  1: completed
task_status = [-1] * n
# -1: not assigned
#  k: assigned task k (1 <= k <= N)
member_status = [-1] * m
day = 0

task_diff = []
for i in range(n):
    tmp = sum(task_difficulty[i])
    task_diff.append(tmp)

member_empty_num = m

tmp_l = []
for i, dependency in enumerate(task_dependency):
    if len(dependency) == 0:
        # tmp_l.append([len(task_dependency_tmp[i]), i])
        tmp_l.append([len(task_dependency_tmp[i]), task_diff[i], i])
        task_status[i] = -2
# tmp_l.sort(reverse=True)
# tmp_l.sort()
tmp_l = sorted(tmp_l, key=lambda x: x[1])
tmp_l = sorted(tmp_l, key=lambda x: -x[0])

can_execute_task = deque()
for tmp in tmp_l:
    can_execute_task.append(tmp)

while True:
    day += 1
    output = [0]

    # print(day, 'day')

    if member_empty_num != 0 and len(can_execute_task) != 0:
        output = []
        if member_empty_num >= len(can_execute_task):
            for i, status in enumerate(member_status):
                if status != -1:
                    continue
                if len(can_execute_task) != 0:
                    _, _, tmp_task = can_execute_task.popleft()
                    output.append(i+1)
                    output.append(tmp_task+1)
                    member_status[i] = tmp_task+1
                    task_status[tmp_task] = 0
                    member_empty_num -= 1
                else:
                    break
        else:
            for i, status in enumerate(member_status):
                if status != -1:
                    continue 
                _, _, tmp_task = can_execute_task.popleft()
                output.append(i+1)
                output.append(tmp_task+1)
                member_status[i] = tmp_task+1
                task_status[tmp_task] = 0  
                member_empty_num -= 1


    if len(output) % 2 == 0:
        print(len(output)//2, end=' ')

    str_output = map(str, output)
    print(" ".join(str_output))

    sys.stdout.flush()

    temp = list(map(int, input().split()))

    # if day == 1:
    #     temp = [1, 1]
    # elif day == 2:
    #     temp = [1, 2]
    # elif day == 3:
    #     temp = [0]
    # elif day == 4:
    #     temp = [0]
    # else:
    #     temp = [-1]
    # print('out:', temp)

    # print('member_status', member_status)
    # print('task_dependency', task_dependency)
    # print('task_status', task_status)
    # print('can_execute_task', can_execute_task)
    # print('member_empty_num', member_empty_num)
    # print('===================')

    if len(temp) == 1:
        if temp[0] == -1:
            exit()
    else:
        for i in range(temp[0]):
            m = temp[i+1]
            t = member_status[m-1]
            member_status[m-1] = -1
            member_empty_num += 1
            task_status[t-1] = 1
            for j, task in enumerate(task_dependency):
                if t-1 in task:
                    task_dependency[j].remove(t-1)

        tmp_l = []
        for i, dependency in enumerate(task_dependency):
            if len(dependency) == 0 and task_status[i] == -1:
                # tmp_l.append([len(task_dependency_tmp[i]), i])
                tmp_l.append([len(task_dependency_tmp[i]), task_diff[i], i])
                task_status[i] = -2

        for tmp in can_execute_task:
            tmp_l.append(tmp)
        # tmp_l.sort(reverse=True)
        # tmp_l.sort()
        tmp_l = sorted(tmp_l, key=lambda x: x[1])
        tmp_l = sorted(tmp_l, key=lambda x: -x[0])

        can_execute_task = deque()
        for tmp in tmp_l:
            can_execute_task.append(tmp)

    # print('member_status', member_status)
    # print('task_dependency', task_dependency)
    # print('task_status', task_status)
    # print('can_execute_task', can_execute_task)
    # print('member_empty_num', member_empty_num)