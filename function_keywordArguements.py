def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")
def dash():
	print(40*'-','\n')

print("This is the O/p when I/p is\n","parrot(1000)")
dash()
parrot(1000)                                        # 1 positional argument

print("This is the O/p when I/p is\n","parrot(voltage=1000)")
dash()
parrot(voltage=1000)                                  # 1 keyword argument

print("This is the O/p when I/p is\n","parrot(voltage=1000000, action='VOOOOOM')")
dash()
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments

print("This is the O/p when I/p is\n","parrot(action='VOOOOOM', voltage=1000000)")
dash()
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments

print("This is the O/p when I/p is\n","parrot('a million', 'bereft of life', 'jump')")
dash()
parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments

print("This is the O/p when I/p is\n","parrot('a thousand', state='pushing up the daisies')")
dash()
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword

parrot()                     # required argument missing
parrot(voltage=5.0, 'dead')  # non-keyword argument after a keyword argument
parrot(110,voltage=220)      # duplicate value for the same argument
parrot(actor='John Cleese')  # unknown keyword argument