#From the Computing for Biologits: Chapter 1 Chapter Problem - gcContent.pys
from twoSalDNAs import *
# inIsland and outsideIsland
#>>> gcContent(inIsland)
#0.4275 
#>>> gcContent(outsideIsland)
#0.5427

# This is a program used to calculate the
# GC Content, now for all DNA strings of any lengh.
def gcContent(DNA):
    ''' Computes the GC content of a DNA string, 
        now of any lenghth.''' 
    count = 0;
    for i in range(len(DNA)):
        if(DNA[i] == "G" or DNA[i] == "C"):
            count += 1;
    print(count / len(DNA));

#from Computing For Biologists: Chapter 1 Exercises 1 - count.py
def count(letter, string):
    ''' This function count takes in a letter,
        or string with just 1 symbol in it, and
        return the number of instances of that
        letter in the input string. '''
    #Itierate through the input string
    count = 0;
    for i in range(len(string)):
        if( string[i] == letter):
            count  += 1; 
    print(count);
    
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
