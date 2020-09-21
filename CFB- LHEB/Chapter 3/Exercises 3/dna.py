#From the Computing for Biologists: Chapter 3
#Chapter Exercise: Section 3.3: DNA and amino acids
#Several Helper Functions - manipulate DNA seqs: dna.py
#Function:  compBase(N), revers(s), reverseComplement(DNA)
from aminoAcids import *
def compBase(N) :
    ''' This helper function compBase(fileName) is 
        used to read in a single nucleotide base
        and return its complementary base. '''
    if N == "T":
        return "A"
    if N == "A":
        return "T"
    if N == "C":
        return "G"
    if N == "G":
        return "C"
def reverse(s) :
    ''' This helper function reverse(s) is 
        used to read in a string and returns
        the reverse of the string. '''
    outputString = "";
    for index in s:
        outputString = index + outputString;
    return outputString;
def reverseComplement(DNA) :
    ''' This helper function reverseComplent(s) 
        is used to read in a DNA string and 
        returns reverse sequence of the 
        complementary string. '''
    complementaryString= "";
    for index in DNA: #Calling compBase to get complementary bases. 
        complementaryString = complementaryString + compBase(index);
    # Calling reverse to return final 'reverse complement'. 
    return reverse(complementaryString); 
def amino(codon) :
    ''' This helper function amino(codon) 
        is used to read in a codon string of
	    3 letters and return the corresponding
        amino acid. '''
    index = 0;
    #A solution starter option: for index in range(len(aa)): 
    for string in aa:
        if codon in codons[index]:
            ''' print(aa[index]); '''
            return(aa[index]);
        else:
            index = index + 1; 
def showOff():
    ''' Prints all of the amino acids '''
    ''' Sample amino list printing function ''' 
    print ("I know ALL the amino acids!")
    for amino in aa: #<-- aa is available to us because we've imported aminoAcids
        print ("Here's an amino acid ", amino); 
def codingStrandToAA(DNA):
    ''' This helper function called
        codingStrandToAA(DNA) will read
        in a sequence of DNA nucleotides
        from the coding strand, and returns the
        corresponding amino acids as a string. 
        Do not worry about start and stop codons. '''
    codedAminos = ""; #Will contain final string of encoded aminos
    for char in range(0, len(DNA), 3):
        codedAminos = codedAminos + amino(DNA[char:char+3]) 
    return(codedAminos) 