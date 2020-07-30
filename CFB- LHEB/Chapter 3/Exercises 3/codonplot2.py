#From the Computer for Biologists: Chapter 3
#Chapter Exercise: Section 3.1: Plotting
#Start Codon Frequencies Using Pyplot
#codonplot.py
#Function:  plotStartCodons(length, trials, steps)

from starts import *
# Learning to use a versatile Python module "matplotlib"
# for plotting data.

import matplotlib.pyplot as plt
# import matplotlib.pyplot as plt2

def plotStartCodons(length, trials, steps) :
    ''' This function plotStartCodons(length, trials, steps)
        calls the startCodons(GCcontent, length, trials)
        function, which calls genString(GCcontent, length)
        '''
    
    gcContent =  0.0 ;      # 0.0 < gcC < 1.0
    xCoordsList = [ ] ;          # List for X plots gcContents     
    yCoordsList = [ ] ;          # List for Y plots start-codon freqs
    
    for r in range(steps) :
        gcContent = r / steps ;
        
        # GCcontents to plot on X axis
        xCoord = gcContent ;
        # Start Codon Frequencies to plot on Y axis. 
        yCoord = round((startCodons( gcContent, length, trials )), 3) ;

        # Percent of Start-Codons for step instance.
        #yCoord = round( (yCoord * 100.0)  ) ;

        
        xCoordsList.append(xCoord) ;
        yCoordsList.append(yCoord) ;
        
    print(" ");
    print(xCoordsList) ;
    print(yCoordsList) ;
    print(" "); 
 #   myXcoords = [0, 0.5, 1.0, 1.5] ;
 #   myYcoords = [10, 12, 6, 23] ;   
#   plt.plot(myXcoords, myYcoords) ;
#    plt.show ( ) ;

#    myXcoords = [0, 1.0, 2.0, 3.5];
 #   myYcoords = [15, 17, 2, 20] ;    
#    plt2.plot(myXcoords, myYcoords) ;
 #   plt2.show ( ) ;

    plt.plot(xCoordsList, yCoordsList) ;
    plt.show ( ) ; 
