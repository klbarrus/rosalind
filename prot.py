#!/usr/bin/env python
# Rosalind Translating RNA into Protein

import itertools

rna_codon = {
    'UUU' : 'F',    'CUU' : 'L', 'AUU' : 'I', 'GUU' : 'V',
    'UUC' : 'F',    'CUC' : 'L', 'AUC' : 'I', 'GUC' : 'V',
    'UUA' : 'L',    'CUA' : 'L', 'AUA' : 'I', 'GUA' : 'V',
    'UUG' : 'L',    'CUG' : 'L', 'AUG' : 'M', 'GUG' : 'V',
    'UCU' : 'S',    'CCU' : 'P', 'ACU' : 'T', 'GCU' : 'A',
    'UCC' : 'S',    'CCC' : 'P', 'ACC' : 'T', 'GCC' : 'A',
    'UCA' : 'S',    'CCA' : 'P', 'ACA' : 'T', 'GCA' : 'A',
    'UCG' : 'S',    'CCG' : 'P', 'ACG' : 'T', 'GCG' : 'A',
    'UAU' : 'Y',    'CAU' : 'H', 'AAU' : 'N', 'GAU' : 'D',
    'UAC' : 'Y',    'CAC' : 'H', 'AAC' : 'N', 'GAC' : 'D',
    'UAA' : '',     'CAA' : 'Q', 'AAA' : 'K', 'GAA' : 'E',
    'UAG' : '',     'CAG' : 'Q', 'AAG' : 'K', 'GAG' : 'E',
    'UGU' : 'C',    'CGU' : 'R', 'AGU' : 'S', 'GGU' : 'G',
    'UGC' : 'C',    'CGC' : 'R', 'AGC' : 'S', 'GGC' : 'G',
    'UGA' : '',     'CGA' : 'R', 'AGA' : 'R', 'GGA' : 'G',
    'UGG' : 'W',    'CGG' : 'R', 'AGG' : 'R', 'GGG' : 'G', 
}

def grouper(iterable, n, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return itertools.zip_longest(*args, fillvalue=fillvalue)

with open("./rosalind_prot.txt") as f:
    rna = f.read().replace('\n','')
f.close()

prot = ""
for seq in grouper(rna,3):
    lookup = ''.join(seq)
    prot += rna_codon[lookup]

print("{}".format(prot))
