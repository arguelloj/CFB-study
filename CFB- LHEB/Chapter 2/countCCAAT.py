#This function is used to count the number of CAT boxes found in a specific DNA sequence.
def countCCAAT(DNAstring):
    ''' This function will iterate through the input DNA sequence and count all the CCAAT box
        motifs near transcription of a gene and return the total. '''
    counter = 0
    for index in range(len(DNAstring)):
        if DNAstring[index:index + 5] == 'CCAAT':
            counter = counter + 1;
    #return counter of CAT box total :)
    return counter
