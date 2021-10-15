
def factorial( num ):
    if num == 1:
        return num
    else:
        print( num, "*" )
        return num * factorial( num - 1 )

result = factorial( 5 )

print( result )