#!/usr/bin/env python
# Rosalind Finding a Motif in DNA

with open("./rosalind_subs.txt") as f:
    s1 = f.readline().rstrip()
    s2 = f.readline().rstrip()
f.close()
for i in range(0,len(s1)):
    if s1[i:i+len(s2)] == s2:
        print("{}".format(i+1), end=' ')
