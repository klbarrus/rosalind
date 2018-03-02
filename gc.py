#!/usr/bin/env python
# Rosalind Identifying Unknown DNA Quickly

with open("./rosalind_gc.txt") as f:
    gc = -1
    clen = 0
    maxgc = 0
    maxname = ""
    for line in f:
        if line[0] == '>':
            name = line[1:].rstrip()
            if gc >= 0:
                gc_cont = gc / clen
                if gc_cont > maxgc:
                    maxgc = gc_cont
                    maxname = name
                gc = -1
                clen = 0
        else:
            dna = line.rstrip()
            gc += (dna.count('G') + dna.count('C'))
            clen += len(dna)
f.close()
print("{}".format(maxname))
print("{0:.6f}".format(maxgc*100))
