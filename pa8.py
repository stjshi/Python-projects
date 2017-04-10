#Stepanie Shi (stjshi)
#Pair programming partner: Christian Lam (ctlam)
#Pa 8

def inc(n):
	return n+1

def dec(n):
	return n-1

def add(a, b):
	if b == 0:
		return a
	else:
		return add(inc(a), dec(b))
def mul(x, y):
	if x == 0 or y == 0:
		return 0
	else:
		return add(x, (mul(x, dec(y))))

i = int(input())
j = int(input())
print(mul(i,j))