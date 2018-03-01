#!/usr/bin/env python
# Rosalind Transcribing DNA into RNA 

with open("./rosalind_rna.txt") as f:
    t = f.read().rstrip()
f.close()
u = t.replace('T','U')
print("{}".format(u))