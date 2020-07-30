#From the Computing for Biology: Chapter 2
#Chapter Problem: GC Content Windows -  gcwindows.py
from salGenomicRegion import * #Contains Salmonella
from gcContent import *  #cContains the gc content calculation
def gcWin(DNA, stepLen) :   
    ''' This function gcWin(DNA, stepLen) takes a DNA string
        as input, and for each DNA sequence of length stepLen, the
        GC content is calculated, and the value is printed out. '''
    
    #for sequence in DNA :
    for index  in range(0, len(DNA), stepLen) :
        #print (index)
        print (gcContent(DNA[index : index + stepLen] ) ) ;
        #gcC = gcContent(DNA[index : stepLen : 1]) ;     
def countPattern(pattern, string) :
    ''' countPattern(pattern, string)  function takes a string as
        input and the input pattern to search for, in that string,
        and returns the number of times that pattern appears. '''
    count = 0;
    for index in range( len(string)) :
        if (string[index: index + len(pattern)] == pattern) :
            count = count + 1 ;
    return(count) ;
###################################################
def countLength(DNAlist, length):
    ''' countLength takes input of a list DNA of
        strings DNAlist and integer, and returns
        how many string are of the length of the input
        integer. '''
    count = 0;
    for i in range(len(DNAlist)):
        if (len(DNAlist[i]) == length):
            count += 1;
    return(count);

def getLength(DNAlist, length):
    ''' getLength takes input of a list of DNA
        strings, DNAlist, and integer, and returns
        a lsit of  string are that are equal to the
        length of the input integer. '''
    outDNAlist = [ ] ;
    for sequence in DNAlist:   
        if (len(sequence) == length):
            outDNAlist = outDNAlist + [sequence];  # || DNAlist[i];? append() too
    print(outDNAlist) ;
def factorial(n):
    '''This function factorial(n) is to calcualte the Factorial
        of a number n, which is the product of n * (n - 1) *
        (n - 2) * (n - 3) * .... 1.  '''
    factorial = 1;
    if (n == 0 or n == 1) :
        return(" Factorial of n is: 1");
    for i in range(n) :
        #print(i);
        factorial = factorial * (i + 1);
        #print(str(i) + " and "  + str(factorial));
    print("Factorial of n is: " +  str(factorial));
