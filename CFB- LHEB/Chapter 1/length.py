# This is a program used to calculate the length of a string.
def length(myString):
    ''' Computes the length of its input string.'''
     
    counter = 0; 
    for myCharacter in myString:
        counter = counter + 1;
    return counter;
