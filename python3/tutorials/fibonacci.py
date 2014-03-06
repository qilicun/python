# -*- coding: utf-8 -*-
#!/usr/bin/env python3
def fib(n):
    """This a simple fibonacci function"""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
#        print(a, end=' ')
        a, b = b, a+b
    return result
print(fib.__doc__)
fib = fib(100)
print(fib)
