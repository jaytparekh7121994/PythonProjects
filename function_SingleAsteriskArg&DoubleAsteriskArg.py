def cheeseshop(kind, *arguments, **keywords):
    """ Kind= Ham meaning compulsory argument
        *arguments = Option, "Would...." and Rhyme
        **keywords= Shopkeeper="Jay", empid= "345678", Order= "547"
    """
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])


Ham = "Hamburger"
Option = "But Sir we have Cheese Burst"
Rhyme = "Hickory Dickory Dock a Mouse went up the clock"
caller = cheeseshop(Ham, Option, "Would Mahi like a bit of a byte?", Rhyme, Shopkeeper="Jay", empid="345678", Order="547")
