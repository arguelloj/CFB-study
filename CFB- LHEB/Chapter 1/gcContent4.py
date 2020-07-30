def GCcontent4(DNA):
    ''' Computes the GC content of a DNA string of lenghth 4.'''
    counter = 0;
    if DNA[0] == 'G' or DNA[0] == 'C':
            counter = counter + 1;
    if DNA[1] == 'G' or DNA[1] == 'C' : 
        counter = counter + 1;
    if DNA[2] == 'G' or DNA[2] == 'C':
        counter = counter + 1;   
    if DNA[3] == 'G' or DNA[3] == 'C':
        counter = counter + 1;
    return counter / 4.0;
