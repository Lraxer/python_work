# Fibonacci sequence implementation
# A simple dynamic programming problem

# fib(n)=1, n=1 or 2
#       =fib(n-1)+fib(n-2), n!=1, n!=2

def Fibonacci(n:int):
    fib = [1,1]
    for i in range(2, n):
        fib.append(fib[i-1]+fib[i-2])

    print(fib)

if __name__ == "__main__":
    Fibonacci(10)