def quick_mod(a:int, x:int, n:int) -> int:
    result = 1
    while(x!=0):
        if(x&1==1):
            result = (result*a)%n
        x = x >> 1
        a = (a*a)%n
    return result

print(quick_mod(20,37,77))