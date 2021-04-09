from functools import wraps
from timeit import repeat


def hashDict(dict):
	return ' '.join([str(val) for val in dict.values()])

def myCache(func):
	saved = {}
	@wraps(func)
	def new_func(*args, **kwargs):
		hashed = hashDict(kwargs)
		if (args, hashed) in saved:
			return saved[(args, hashed)]
		saved[(args, hashed)] = func(*args, **kwargs)
		return saved[(args, hashed)]
	return new_func

@myCache
def fibs(n):
	'''Is this the only docstring now''' 
	if n == 0:
		return 1
	elif n == 1:
		return 1
	else:
		return fibs(n-1) + fibs(n-2)

setup_code = "from __main__ import fibs"
stmt = "fibs(n=40)"
times = repeat(setup=setup_code, stmt=stmt, repeat=3, number=3)
print(min(times))


kwd_mark = object()     # sentinel for separating args from kwargs
# (a, ) is how you write a single element tuple. You can only concatenate tuples, not add ints/strs to tuples
# Used in actual functools.lru_cache codebase to cache dictionaries.
def cached_call(*args, **kwargs):
    key = args + (kwd_mark,) + tuple(sorted(kwargs.items()))
    return cache.get(key)

