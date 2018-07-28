# May Pena
# This program opens a file containing the script to the play
# "A Streetcar Named Desire" and analyses the file in order
# to find which character mentioned another one the most. 

def main():
#   Open file and read it
    print("Please enter a text file name below, such as test.txt")
    user = input( "File name: " )
    file = open( user, "r" )
    text = file.readlines()
    print()
    
#   Blance = B, Stella = S, Stanley = T
#   How many times Stanley mentions Blanche or Stella
    TBcount = 0
    for line in text:
        if line.startswith( "STANLEY:" ):
            TBcount = TBcount + line.count( "Blanche" )           
    TScount = 0
    for line in text:
        if line.startswith( "STANLEY:" ):
            TScount = TScount + line.count( "Stella" )           

    
#   How many times Blanche mentions Stella or Stanley
    BScount = 0
    for line in text:
        if line.startswith( "BLANCHE:" ):
            BScount = BScount + line.count( "Stella" )           
    BTcount = 0
    for line in text:
        if line.startswith( "BLANCHE:" ):
            BTcount = BTcount + line.count( "Stanley" )           
    

#   How many times Stella mentions Blanche or Stanley
    SBcount = 0
    for line in text:
        if line.startswith( "STELLA:" ):
            SBcount = SBcount + line.count( "Blanche" )           
    STcount = 0
    for line in text:
        if line.startswith( "STELLA:" ):
            STcount = STcount + line.count( "Stanley" )
            

# Print references
    print( "Stanley -> Blanche = ", TBcount )
    print( "Stanley -> Stella  = ", TScount )
    print( "Blanche -> Stella  = ", BScount )
    print( "Blanche -> Stanley = ", BTcount )
    print( "Stella -> Stanley  = ", STcount )
    print( "Stella -> Blanche  = ", SBcount )
    


# Who refers to another character the most
    referals = [ TBcount, TScount, BScount, BTcount, SBcount, STcount ]

    if max( referals ) == 0:
        print( "No references" )
    
    elif max( referals ) == TBcount:
        print( "Stanley mentioned Blanche the most! " )
        
    elif max( referals ) == TScount:
        print( "Stanley mentioned Stella the most!  " )
        
    elif max( referals ) == BScount:
        print( "Blanche mentioned Stella the most!  " )
            
    elif max( referals ) == BTcount:
        print( "Blanche mentioned Stanley the most! " )
            
    elif max( referals ) == SBcount:
        print( "Stella mentioned Blanche the most!  " )
            
    elif max( referals ) == STcount:
        print( "Stella mentioned Stanley the most!  " )

  

main()
