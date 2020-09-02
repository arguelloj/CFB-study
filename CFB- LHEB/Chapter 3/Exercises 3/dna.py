#From the Computer for Biologists: Chapter 3
#Chapter Exercise: Section 3.3: DNA and amino acids
#Several Helper Functions - manipulate DNA seqs: dna.py
#Function:  compBase(N), revers(s), reverseComplement(DNA)
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

    
 