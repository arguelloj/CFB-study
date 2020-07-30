
#From the Computing for Biology: Chapter 2
#Section 2.5 Counting Patterns -  countPattern.py

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
        if (len(i) == length):
            outDNAlist = outDNAlist + [sequence];  #or DNAlist[i];?? append() too
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
