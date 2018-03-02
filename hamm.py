#!/usr/bin/env python
# Rosalind Evolution as a Sequence of Mistakes

with open("./rosalind_hamm.txt") as f:
    s1 = f.readline().rstrip()
    s2 = f.readline().rstrip()
f.close()
hd = 0
for a,b in zip(s1,s2):
    if a != b:
        hd += 1
print("{}".format(hd))
