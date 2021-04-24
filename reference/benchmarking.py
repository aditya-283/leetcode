from functools import cache
from timeit import repeat


def fib1(n):
	'''Is this the only docstring now''' 
	if n == 0:
		return 1
	elif n == 1:
		return 1
	else:
		return fib1(n-1) + fib1(n-2)

@cache
def fib2(n):
	'''Is this the only docstring now''' 
	if n == 0:
		return 1
	elif n == 1:
		return 1
	else:
		return fib2(n-1) + fib2(n-2)


setup_code = "from __main__ import fib1, fib2"
stmt = "fib2(n=40)"
times = repeat(setup=setup_code, stmt=stmt, repeat=3, number=3)
print(min(times))