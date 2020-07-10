import math
# 求原根

def quick_mod(a:int, x:int, n:int) -> int:
    result = 1
    while(x!=0):
        if(x&1==1):
            result = (result*a)%n
        x = x >> 1
        a = (a*a)%n
    return result

def Isprime(mnum): #质数判断
    sqrmnum = math.floor(math.sqrt(mnum))
    flag = True
    if mnum%2==0 and mnum!=2:
        return not flag
    else:
        for i in range(2, sqrmnum+1):
            cle = mnum%i
            if cle==0:
                flag = False
                break
            else:
                continue
        return flag

def Iscoprime(num1, num2): #互素判断-欧几里得算法
    if num1<num2:
        tmp = num1
        num1 = num2
        num2 = tmp
    while num1%num2!=0:
        a = num2
        num2 = num1%num2
        num1 = a
    
    if num2!=1:
        return False
    else:
        return True

def Prime_fac(mnum):     #素因子分解，重复的素因子也包含在内
    if not isinstance(mnum, int):
        raise TypeError     #引发异常
    f1 = []
    p = 2
    pl = []
    while p*p <= mnum:
        if (p in pl) or Isprime(p):
            if not p in pl:
                pl.append(p)
            if mnum%p == 0:
                f1.append(p)
                mnum = mnum // p      #做除法后向下取整，但是变量类型不会强制转换为int
                # print(p, mnum)
                # f1.extend(Prime_fac(mnum))   #可以用这一行做递归来求，也可以用11行以后的非递归求
            else:
                if p == 2:
                    p = p+1
                else:
                    p = p+2
        else:
            if p == 2:
                p = p+1
            else:
                p = p+2
    f1.append(mnum)
    # print(pl)
    return f1

def Getfac(mnum):   #求出phi，以及phi的因子、phi除以因子的商，传递给计算原根的函数
    if Isprime(mnum):
        phi = mnum-1
    else:
        fac = Prime_fac(mnum)
        distfac = list(set(fac))
        phi = mnum
        for i in distfac:
            phi = int(phi*(1-1/i))
    phifac = Prime_fac(phi)
    distphifac = list(set(phifac))
    q = []
    for j in distphifac:
        q.append(int(phi/j))
    
    print(q)

    return q


def PRoot(mnum, q): #a是因子个数，b是要计算的指数
    count = []
    for i in range(2, mnum):
        if Iscoprime(mnum, i) :
            flag = True
            for j in q:
                check = quick_mod(i, j, mnum)
                # show process
                print(str(i) + '^' + str(j) + ' mod ' + str(mnum) + ' = ' + str(check) + '\n')
                if check==1:
                    flag = False
                    break
            if flag==True:
                count.append(i)
        else:
            continue
    print(count)
    print('原根共有'+str(len(count))+'个.')

def GetPRoot(mnum):
    q = Getfac(mnum)
    PRoot(mnum, q)

if __name__=='__main__':
    while True:
        a = input("输入需要计算的数字：")
        a = int(a)  
        GetPRoot(a)