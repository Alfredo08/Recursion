
def printHello( num ):
    if num == 0:
        return 0
    else:
        print( "Hello world!" )
        return printHello( num - 1 )

printHello( 5 )