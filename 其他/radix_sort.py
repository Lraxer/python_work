# 基数排序
def radix_sort(a:list):
    bucket = [[] for i in range(10)]
    exp = 1
    maxnum = max(a)
    while maxnum//exp!=0 :
        for num in a:
            bucket[(num//exp)%10].append(num)
        a.clear()
        for x in bucket:
            for y in x:
                a.append(y)
            x.clear()
        exp = exp*10

# if __name__ == '__main__':
#     a = [334,5,67,345,7,345345,99,4,23,78,45,1,3453,23424]
#     radix_sort(a)
#     print(a)