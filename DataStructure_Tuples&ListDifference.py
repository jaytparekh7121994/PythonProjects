""" Tuples, list and range are Sequence type"""

tupl = 12345, 54321, "hello", "Statement can be saved in tuples", 1.0, 3.4567
print(tupl)
# tupl[0] = 34521
# print(tupl) TypeError: tuple object doesnt not support item assignment
# Tuples are immutable

lis = [12345, 54321, "hello", "Statement can be saved in tuples", 1.0, 3.4567]
print(lis)
lis[0] = 34521

print(lis)
# Reflect changes @lis[0] position
# list are mutable

x, y, z, w, u, v = tupl
print("x =", x, "y =", y, "z =", z, "w =", w, "u =", u, "v =", v)
# Unpacking or assigning the tuples to different variables

x, y, z, w, u, v = lis
print("x =", x, "y =", y, "z =", z, "w =", w, "u =", u, "v =", v)
# Assigning the list to different variables
