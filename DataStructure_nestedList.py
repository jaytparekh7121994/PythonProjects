combs = []

for i in [1, 2, 3]:
    for j in [3, 2, 1]:
        combs.append((i, j))
        # combs.append(i,j) shows error that append can take only one argument.
        # Add parantheses to i,j -> (i,j) ,it makes it a tuple.
        # Hence, its just one object passed in append()
print(combs)

print("looping list within list and printing the tuple which is in ()")
print(40 * "-")

"""-------------------------------------------------------------------------"""

""" Nested List Example :"""

matrix = [
    ["Sunday", "Saturday"],
    ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
    ["Holi", "Diwali", "Eid", "Christmas", "Lohri"]
    ]

print([[row[i] for row in matrix]for i in range(2)])
print("End of Single line transpose")
print(40 * "-")

""" ------------------------------------------------------------------------"""

transposed = []
for i in range(2):
    print("i = ", i)
    # the following 3 lines implement the nested listcomp
    transposed_row = []
    for row in matrix:
        print("Row", row, "of", i, "is", row[i])
        # for i=0 each rows first element will be returned
        # for i=1 each rows second element will be returned
        transposed_row.append(row[i])
    transposed.append(transposed_row)

print("transposed =", transposed)

print("End of multiple looping transpose", '\n', 40 * "-")
