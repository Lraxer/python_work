# Eculidean Algorithm
#! a must be greater than b
def gcd_recursive(a, b):
	"""递归的欧几里得算法"""
    if b==0:
        return a
    else:
        return gcd_recursive(b,a%b)

def gcd_nonrecursive(a,b):
	"""非递归的欧几里得算法"""
	while b:
		a, b = b, a%b
	return a

def gcd_extentsion_recursive(a, b):
	"""递归的扩展欧几里得算法"""
    if b==0:
        return (a, 1, 0)
    else:
        (r, x, y) = gcd_extentsion_recursive(b, a%b)
        t = x
        x = y
        y = t-(a//b)*y
        return (r, x, y)
    
def gcd_extentsion_nonrecursive(a, b):
	"""非递归的扩展欧几里得算法"""
    prevx, x=1,0
    prevy, y=0,1
    while b:
        q=a//b
        x, prevx = prevx-q*x, x
        y, prevy = prevy-q*y, y
        a, b = b, a%b
    return (a, prevx, prevy)