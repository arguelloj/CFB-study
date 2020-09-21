#From Computing for Biologists: Chapter 3
#Chapter Exercise: Section 3.2: Loading 
#FAFSTA file into Python Code: load.py
#Function: loadSeq(fileName)     
# >>> salSeq = loadSeq("U81861.fna")
# >>> len(salSeq)
# 1880
# >>>
def loadSeq(fileName) :
    ''' This function loadSeq(fileName) is used to
        read in a text file, .fna FAFSTA file into
        Python for curation and possible analysis. '''
    f = open(fileName) # Open the file
    linesList = f.readlines() # Read in the file as a list of its lines
    f.close() # Close the file

    newList=[]  # A new list!
    for line in linesList :  # For each line in our linesList. To create
        newList.append(line[:-1])  # SLICE off the last character and append the truncated string to the newList. '''

    DNAstring = ""; 
    index = 1; 
    # For line in newList: To create 1 single DNA string to return
    for line in newList:
        if  '>' in line: 
                '''This is a comment - effectively a pass. Ignore label line newList[0] '''
        else:
                DNAstring = DNAstring + newList[index];
                index = index + 1 ;
    return(DNAstring);