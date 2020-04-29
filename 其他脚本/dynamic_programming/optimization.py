# A simple dynamic programming problem
# 假设有8个任务，分别位于不同时段，完成任务有一定奖金。
# Task      Time    reward
# 1         1-4     5
# 2         3-5     1
# 3         0-6     8
# 4         4-7     4
# 5         3-8     6
# 6         5-9     3
# 7         6-10    2
# 8         8-11    4
# 任务必须做完才能得到奖金。一个时段只能做一个任务。
# 要求规划时间和任务，求出拿到最多奖金的方法。

# Opt(n) = max(
#   reward+Opt(prev(n)), 
#   Opt(n-1)
# )
# 其中，n代表的task是按结束时间的顺序由低到高排列好的。prev(n)代表在task n开始前就结束的最近的task。
# 问题的本质是求Opt(8)

def getprev(ttime:list)->list:
    prev = []
    for i in range(len(ttime)):
        j = i-1
        while j>=0:
            if ttime[i][0]>=ttime[j][1]:
                prev.append(j)
                break
            else:
                j=j-1
        if j==-1:
            prev.append(j)
    return prev


def findopt(task:list, ttime:list, reward:list):
    prev = getprev(ttime)
    Opt = []
    trace = []
    for i in range(len(task)):
        if prev[i]==-1:
            choice1 = reward[i]
        else:
            choice1 = reward[i]+Opt[prev[i]]

        if i==0:
            choice2 = 0
        else:
            choice2 = Opt[i-1]
        
        # 直接输出最优结果
        # Opt.append(max(choice1, choice2))

        # 输出最优结果的路径 
        if choice1>choice2:
            Opt.append(choice1)
            if prev[i]==-1:
                trace.append([i])
            else:
                #! 一定要切片，不然只是浅复制
                trace.append(trace[prev[i]][:])
                trace[i].append(i)
        else:
            Opt.append(choice2)
            if i==0:
                trace.append([i])
            else:
                #! 一定要切片，不然只是浅复制
                trace.append(trace[i-1][:])
    
    return Opt, trace

if __name__ == "__main__":
    task = [i for i in range(1,9)]
    ttime = [
        (1, 4), (3, 5), (0, 6), (4, 7),
        (3, 8), (5, 9), (6, 10), (8, 11)
    ]
    reward = [5,1,8,4,6,3,2,4]

    # print(getprev(ttime))

    Opt, trace = findopt(task, ttime, reward)
    print(Opt)
    print(trace)