A_dict = {'Key4': 126, 'Key5': 124, 'Key3': 125}
print(sorted(A_dict))
# Sorted will sort the keys alphabetically

for k in A_dict:
    print(k)
    # to retrieve Keys use K in A_dict
    # if we want Key:Value pair use k,v in A_dict.items()

A_list = [('key3', 'value1'), ('key2', 'value3')]
print(dict(A_list))
# technique to create a dict using list and dict keyword
# Gives a sorted dictionary

dic = dict(bsape=4093, aguido=4099, jack=5000)
# Defining the dictionary using dict keyword
print(dic)  # Gives a sorted dictionary
