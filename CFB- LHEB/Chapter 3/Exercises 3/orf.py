#From the Computing for Biologists: Chapter 3
#Chapter Exercise: Section 3.3: DNA and amino acids
#Several Helper Functions - manipulate DNA seqs: dna.py
#Function:  compBase(N), revers(s), reverseComplement(DNA)
from aminoAcids import *

from dna import *

def restOfORF(DNA):
    ''' This helper function called
    restOfORF(DNA) will read in a 
    sequence of DNA nucleotides from the
    coding strand, and returns the
    corresponding amino acids as a string. 
    Do not worry about start and stop codons. ''' 
    outputORFstring = ""; #Data curation string for DNA seq
    for char in range(0, len(DNA), 3): 
        if DNA[char:char+3] in ['TAG', 'TAA', 'TGA']:
            return(outputORFstring); #Return ORF up to Stop Codon
        else:
            outputORFstring = outputORFstring + DNA[char:char+3]; #Prep of output ORF string
    return(outputORFstring);