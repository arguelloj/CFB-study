#from Computing For Biologists: Chapter 1 Exercises 1 -  elif.py
def ORFadvisor(DNA) :
    ''' This function ORFadvisor(DNA) takes in a
        string of DNA as input and will prompt
        the user if they have complied with the
        3 requirements of a strand of DNA to be ORF.'''
    if(len(DNA) % 3 == 0  and  
       DNA[0: 3: 1] == 'ATG' and 
       (
            (DNA[len(DNA) - 3:   len(DNA):   1] == 'TGA' ) or
            (DNA[len(DNA) - 3:   len(DNA):   1] == 'TAG' ) or
            (DNA[len(DNA) - 3:   len(DNA):   1] == 'TAA' )
        )
       ):
        return ("This is an ORF")
    elif(DNA[0: 3: 1] != 'ATG'):
        return ("The first three bases are not ATG")
    elif(   DNA[len(DNA) - 3:   len(DNA):   1] != 'TGA'  and  #DONT forget that AND is vital, NOT or
            DNA[len(DNA) - 3:   len(DNA):   1] != 'TAG'  and  #DONT forget that AND is vital, NOT or
            DNA[len(DNA) - 3:   len(DNA):   1] != 'TAA' 
        ):
        return ("The last 3 bases are not a STOP codon")
    else:
        return ("The string is not of the correct length")

def friendly(greeting):
    ''' This function friendly(greeting) take in a
        greeting from user as input and then returns
        a greeting to screen based on the user input.
        Must say Hello or Hi, ask a question, else
        it is not understandable.'''
    if(greeting[0: 2: 1] == "Hi" or
       greeting[0: 5: 1] == "Hello"):
        return("Hey there, did you have a happy Mother's Day?")
    elif(greeting[len(greeting) - 1] == "?"):
        return("Good question!") 
    else:
        return("I am sorry, but I did not understand you.")

#from Computing For Biologists - Chapter 1 Exercises 1 ifelse.py
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
    
