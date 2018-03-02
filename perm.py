#!/usr/bin/env python
# Rosalind Enumerating Gene Orders

import math
import itertools

with open("./rosalind_perm.txt") as f:
    num = int(f.read())
f.close()
perms = math.factorial(num)
print("{}".format(perms))
for i in itertools.permutations(range(1,num+1),num):
    print("{}".format(" ".join(map(str,i))))
