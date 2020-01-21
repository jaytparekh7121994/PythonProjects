a = set('abracadabra')
b = set('alacazam')

print("Set a: ", sorted(a))
print("Set b: ", sorted(b))
print("In set a but not b:", sorted(a - b))
# print ("Union of a+b:", a + b) a+b is not supported in sets
print("Either in a or b or both", sorted(a | b))
print("In Both sets a and b:", sorted(a & b))
print("Either in a or b but not in both:", sorted(a ^ b))
