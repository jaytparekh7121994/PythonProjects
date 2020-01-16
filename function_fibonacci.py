
def fibonacci_series(number):
    """ Prints the fibonacci_series uptill the number"""
    a,b = 0,1
    while a < number:
	    print (a,end=",")
	    a,b = b,a+b

fib = fibonacci_series
print(fib(1000))