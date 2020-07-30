#From the Computing for Biologits: Chapter 2
#Section 2.4 Looping Over Lists - looping.py
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
# This is a function used to return the
# strings with the length equal to input
# length "length".
	
##Koder comment
def getLength(DNAlist, length):
    ''' getLength takes input of a list of DNA
        strings, DNAlist, and integer, and returns
        a lsit of  string are that are equal to the
        length of the input integer. '''
    outDNAlist = [ ] ;
    for sequence in DNAlist:   
        if (len(i) == length):
            outDNAlist = outDNAlist + [sequence];  #or DNAlist[i];?? append() too
    print(outDNAlist);

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


