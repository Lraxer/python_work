# A simple dynamic programming problem
# 在一个正数的数组arr中，找到它的子集，使子集的和等于一个特定数值val。
# Opt(n, val) = Opt(n-1, val-arr[n]), 选择arr[n]
#             = Opt(n-1, val), 不选择arr[n]
# 出口：val==0, arr[0]==val
# 建立一个矩阵，行代表arr的元素，长度为len(arr);列为从0到val的数，长度为val+1，矩阵元素为布尔值

# TODO 暂时只能判断存在性，不能得到具体哪些数
import numpy as np 

def find_subset(arr:list, val:int):
    submatrix = np.zeros((len(arr), val+1), dtype=bool)
    submatrix[:,0] = True
    if arr[0]<=val:
        submatrix[0, arr[0]] = True
    # fill the matrix
    for i in range(1, len(arr)):
        for j in range(1, val+1):
            if arr[i]>j:
                submatrix[i, j] = submatrix[i-1, j]
            else:                
                choice1 = submatrix[i-1, j-arr[i]]
                choice2 = submatrix[i-1, j]
                submatrix[i,j] = choice1 or choice2
    
    return submatrix[len(arr)-1, val]

if __name__ == "__main__":
    arr = [3, 34, 4, 12, 5, 2]
    val = 9
    print(find_subset(arr, val))