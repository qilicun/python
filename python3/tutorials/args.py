#!/usr/bin/env python3
def concat(*args, sep='/'):
    return sep.join(args)

print(concat("usr", "bin", "env"))
