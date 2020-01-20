def addition(x, y, default="Addition"):
    print("performing", default, "of", x, y, "\n", 40 * '-')
    total = x + y
    return total


a_list_of_nos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b_list_of_nos = [100, 200, 300, 400, 500, 600, 700, 800]

total_of_both = list(map(addition, a_list_of_nos, b_list_of_nos))
print(total_of_both)

""" Map function will work only if the len(var_a)== len(var_b)for each elememt.
Otherwise, it will map only the smallest of the two lists.
"""
