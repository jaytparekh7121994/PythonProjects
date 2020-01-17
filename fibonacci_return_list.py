def fibonacci_series(number):
    """ Prints the fibonacci_series uptill the number"""
    result = []
    a, b = 0, 1
    while a < number:
        result.append(a)
        a, b = b, a+b
    return result       # return statement must be outside the loop like while

fib = fibonacci_series(2000)

print (fib) 	# Prints the list of fibonacci series
