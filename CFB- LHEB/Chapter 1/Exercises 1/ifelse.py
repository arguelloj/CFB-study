#This is ifelse.py which is the 2nd exerise of chapter 1
#from Computing For Biologists.    

def absolute(n) :
    ''' This function absolute(x) is to take input
        and return the absolute value as output. '''
    #>>> absolute(-3)
    #3
    #>>> absolute(5000000)
    #5000000
    if n < 0:
        return (-n)
    else:
        return (n)

def palindrome4(input):
    ''' This function palindrome4(input) is to take an
        input of a 4 character string and return 
        whether true or false. If not exactly 4 return
        return false as well. '''
    #>>> palindrome4("poop")
    #True
    #>>> palindrome4("dad")
    #False
    #>>> palindrome4("bool")
    #False
    #>>> palindrome4("abba")
    #True
    if (input == input[len(input) - 1: 0:-1] + input[0] and len(input) == 4) :
        return (True)
    else:
        return (False)
    
def ORF(inputDNA):
    ''' This function ORF, Open Reading Frame, is to
        take in a string of DNA as input, and then returns
        the Boolean value True if input fulfills the following 
        3 conditions:
        1) begins with 'ATG',
        2) ends with 'TGA'  or 'TAG' or 'TAA', 
        3) string length is a multiple of 3
    '''
    if(len(inputDNA) % 3 == 0  and  
       inputDNA[0: 3: 1] == 'ATG' and 
       (
            (inputDNA[len(inputDNA) - 3:   len(inputDNA):   1] == 'TGA' ) or
            (inputDNA[len(inputDNA) - 3:   len(inputDNA):   1] == 'TAG' ) or
            (inputDNA[len(inputDNA) - 3:   len(inputDNA):   1] == 'TAA' )
        )
       ):     
        return (True)
    else:
        return(False)
    
################     first.py        ###############
    
def power(x) :
    '''This function power(x) is to take the
        input and set it to the power of the
       input'''
    return ( x ** x)

def stringMultiply(myString, number) :
    ''' This function takes in an input string
        and concatenates the string a specific
        number of times. '''
    #>>> stringMultiply('fernando', 3)
    # 'fernandofernandofernando'
    return (myString * number)

def listMaker(myString, number) :
    ''' This function takes in an input string
        and number and returns new list with a
        concatenated number of copies. '''
    #>>> listMaker('hello fernando', 2)
    #['hello fernando', 'hello fernando']
    return ([myString] * number);

def countCodons (myDNAString) :
    ''' This function takes a DNA string as input
        in multiples of 3, and then returns the
        number of codons in that string. '''
    #>>> countCodons("GCTGCTGCT")
    #3.0
    return (len(myDNAString) / 3)

def palindromeMaker(inputString) :
    ''' This function takes a string as input
        and returns the string followed by its
        reverse. It will work for any length
        string.  '''
    #>>> palindromeMaker("fernando")
    #'fernandoodnanref' 
    return (inputString + inputString[len(inputString) - 1: 0: -1] + inputString[0])
