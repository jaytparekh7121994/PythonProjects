vec = [-4, -2, 0, 2, 4]

print([x for x in vec if x >= 0])   # for loop and conditional statement

lis = []

for x in vec:
    if x >= 0:
        lis.append(x)

print(lis)

print([abs(x) for x in vec])


lis.clear()

for x in vec:
    lis.append(abs(x))

print(lis)


lis.clear()

for x in range(6):
    lis.append((x, x**2))

print(lis)
