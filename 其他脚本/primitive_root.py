# 求原根
def PRoot(mnum, b): #a是因子个数，b是要计算的指数
    count = []
    for i in range(2, mnum):
        iscoprime = mnum%i 
        if iscoprime!=0:
            flag = True
            for j in b:
                check = pow(i,j) % mnum
                print(str(i) + '^' + str(j) + ' mod ' + str(mnum) + ' = ' + str(check))
                if check==1:
                    flag = False
                    break
            if flag==True:
                count.append(i)

        else:
            continue
    print(count)

if __name__=='__main__':
    #PRoot(19, [6,9])