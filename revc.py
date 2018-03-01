#!/usr/bin/env python
# Rosalind Complementing a Strand of DNA

comp = {
    'A' : 'T',
    'T' : 'A',
    'C' : 'G',
    'G' : 'C',
}

with open("./rosalind_revc.txt") as f:
    dna = f.read().rstrip()
f.close()
rdna = dna[::-1]
revc = ""
for base in rdna:
    revc += comp[base]
print("{}".format(revc))