#This function is used to count the number of CAT boxes found in a many
#different inputs of a specific DNA sequence, in one calling of the function.
from countCCAAT import countCCAAT
def multiCountCCAAT(DNAstringList):
    ''' This function will iterate through the given input DNA sequences and count all the
        CCAAT box motifs near transcription of a gene, and print the totals for each input
        sequence. '''
    for DNAstring in DNAstringList:
        print(countCCAAT(DNAstring));        
