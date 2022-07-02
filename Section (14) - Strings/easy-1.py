def is_palindrome(str):  # madam
    for i in range(len(str)//2):
        if str[i] != str[len(str)-i-1]:
            return "NO"
    return "YES"

print(is_palindrome("madam"))
print(is_palindrome("11/11/11"))
print(is_palindrome("12321"))
print(is_palindrome("12341")) 


