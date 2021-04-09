cons = lambda h, t: lambda w:h if w else t
toLL = lambda l: cons(l[0], toLL(l[1:])) if l else None
reverse = lambda l, r=None: reverse(l(False), cons(l(True), r)) if l else r

# Utils
toString = lambda l: str(l(True)) if not l(False) else str(l(True)) + ', ' + toString(l(False))
toStringBracketed = lambda l: '[' + toString(l) + ']'

# Interesting use of iter and map
nth = lambda l, n: None if not l else nth(l(False), n-1) if n>0 else l(True)
toString = lambda l: ', '.join(map(str, iter(lambda n=[0]: nth(l, n.append(n[0]+1) or n.pop(0)) , None)))

# Tests
x = cons(3, cons(2, cons(1, None)))
print(toStringBracketed(reverse(x)))
print(toLL([1, 2, 3])(True))


# Learnings

## False or '' or 3 or 'a' returns first True value that is 3
## iter can be passed a lambda, and a sentitel (terminal) value
## pop always returns the value popped, append returns nothing
## lambdas can be called recursively
## And how cons or the functional way of looking at lists is as options or alternatives. \
   # ties in well with the category theoretic view of the List functor.

