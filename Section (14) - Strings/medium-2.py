# aaabbbccc ⇒ 3a_3b_3c
# ○ z ⇒ z
# ○ aabbbbbddddcccc ⇒ 5b_4c_4d_2a
# ○ aabbccaa ⇒ 2a_2a_2b_2c

def compresse_str(stri):

    if len(stri) == 1:
        return stri
    
    stri += '$'
    new_str = []
    idx = 0
    for i in range(1,len(stri)):
        if stri[i] != stri[i-1]:
            sz = i - idx
            com = str(sz) + stri[i-1]
            new_str.append(com)
            idx = i 
    return sorted(new_str)

print('_'.join(compresse_str('aaabbbccc')))
print(compresse_str('aabbbbbddddcccc'))
print(compresse_str('z'))
  
