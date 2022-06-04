def special_multiplication(string):
    new_string = ""
    for idx, char in enumerate(string):
        stringo = (char * (idx+1))
        new_string += stringo
    return new_string

print(special_multiplication('abcxf'))