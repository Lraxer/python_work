# A simple dynamic programming problem
# 给出一个数组，求出这个数组不相邻元素和的最大值。
# e.g. arr=[1,2,4,1,7,8,3], 最大值为3+7+4+1=15

# Opt(n) = Opt(n-2)+arr[n], 如果选择加arr[n]
#        = Opt(n-1), 如果不选择加arr[n]
# Opt(0) = arr[0], Opt(1) = max(arr[0], arr[1])
# Opt(n)是前n+1个数的最大值

def findopt(arr:list)->list:
    Opt = [arr[0], max(arr[0], arr[1])]
    for i in range(2, len(arr)):
        choice1 = Opt[i-2]+arr[i]
        choice2 = Opt[i-1]
        Opt.append(max(choice1, choice2))
    return Opt

if __name__ == "__main__":
    arr = [1,2,4,1,7,8,3]
    print(findopt(arr))
