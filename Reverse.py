
def reverse( text ):
    if len( text ) == 1:
        return text
    else:
        return text[ len(text) - 1] + reverse(text[0:len(text) - 1])



def reverse2( text, index ):
    if index == 0:
        return text[index]
    else:
        return text[index] + reverse2( text, index - 1 )

text = "hello world"

result = reverse2( text, len( text ) - 1)
print( result )


# Finding if a string is palindrome
# radar => True
# hello => False

# Fibonacci sequence
# 1 1 2 3 5 8 13 21 34 55 ...
# Solve it with an iterative solution
# Then solve it with a recursive solution

# 5 => 1 1 2 3 5
# 7 => 1 1 2 3 5 8 13

# 5 => 5
# 7 => 13

