# This is a program used to calculate the length of a string.
def DNAtoRNA(myDNA):
    ''' Converts a strand of a double helix DNA into an equivalent RNA. T to U nucleotide.'''
     
    RNA = "";
    for nuc in myDNA:
        # When ever there is Thymine in the DNA strand, it is converted to Uracil
        if nuc == 'T':
            RNA = RNA + 'U'
        else:
            RNA = RNA + nuc
    return RNA;
 
