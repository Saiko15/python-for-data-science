dct = dict(zip('abcdefghijklmnopqrstuvwxyz0123456789', 'YZIMNESTODUAPWXHQFBRJKCGVL!@#$%^&*()'))

line = 'acMNmn39'
line2 = 'vwXYZ0123'

for char in line:
    
    print(dct.setdefault(char, char), end='')

print()

for char in line2:
    print(dct.setdefault(char, char), end='')

print(dct) 