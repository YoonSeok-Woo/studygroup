a=['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
croatia = input()

for i in a:
    croatia = croatia.replace(i, '*')
print(len(croatia))