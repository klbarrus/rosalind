#!/usr/bin/env python
# Rosalind Counting DNA nucleotides

dna_count = {
    'A' : 0,
    'C' : 0,
    'G' : 0,
    'T' : 0,
}

with open("./rosalind_dna.txt") as f:
    for line in f:
        for char in line:
            if char == 'A' or char == 'C' or char == 'G' or char == 'T':
                dna_count[char] += 1
f.close()
print("{} {} {} {}".format(dna_count['A'],dna_count['C'],dna_count['G'],dna_count['T']))