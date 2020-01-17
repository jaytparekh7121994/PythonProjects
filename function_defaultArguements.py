""" This code contains the example that the function has the "Default Arguement Values" eg; reminder ="Please try again!" or retries =4 """
def ask_ok(prompt, retries=4, reminder='Please try again!'):
    """ Enter the y, ye or yes or n, no, nop or nope """
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes','Y','Ye','Yes'):
            print("Success")
            return True
        if ok in ('n', 'no', 'nop', 'nope','N','No','Nop','Nope'):
            print("Not Success")
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response') #
        print(reminder)

ask_ok('Do You really want to quit?\n')