# This is a program used to calculate the GC Content for all DNA strings of lengh 1 to 4.
def GCcontent1thru4(DNA):
    ''' Computes the GC content of a DNA string of lenghth 1 through 4.'''
    
    counter = 0; 
    if len(DNA) == 1:
        if DNA[0] == 'G' or DNA[0] == 'C':
            counter = counter + 1;
        return counter / 1.0;
#   Logic to test for only 2 nucleotides in the DNA string. 
    elif len(DNA) == 2:
        if DNA[0] == 'G' or DNA[0] == 'C':
            counter = counter + 1;
        if DNA[1] == 'G' or DNA[1] == 'C' : 
            counter = counter + 1;
        return counter / 2.0; 
#   Logic to test for only 3 nucleotides in the DNA string.         
    elif len(DNA) == 3:
        if DNA[0] == 'G' or DNA[0] == 'C':
            counter = counter + 1;
        if DNA[1] == 'G' or DNA[1] == 'C' : 
            counter = counter + 1;
        if DNA[2] == 'G' or DNA[2] == 'C':
            counter = counter + 1;   
        return counter / 3.0;
#   Logic to test for 4 nucleotides in the DNA string.     
    elif len(DNA) == 4:    
        if DNA[0] == 'G' or DNA[0] == 'C':
            counter = counter + 1;
        if DNA[1] == 'G' or DNA[1] == 'C' : 
            counter = counter + 1;
        if DNA[2] == 'G' or DNA[2] == 'C':
            counter = counter + 1;   
        if DNA[3] == 'G' or DNA[3] == 'C':
            counter = counter + 1;
        return counter / 4.0;
#   Testing if more than 4 nucleotides are entered in the DNA string. '''    
    else:
        return 'I can NOT handle strings less than 1 or longer than 4.'
