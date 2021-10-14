
# 5 =  5 + 4 + 3 + 2 + 1 = 15

def sum( num ):
    if num == 1:
        return 1
    else:
        return num + sum( num - 1)

result = sum( 10 )
print( result )




