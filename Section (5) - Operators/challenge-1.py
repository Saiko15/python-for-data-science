# ● Write a program that reads 3 integers about the class room
# ○ Number of boys (nb), number of girls (ng), number of teachers (nt)
# ● Prepare and print a boolean variable for these cases:
# ● nb greater than 25
# ● ng less than or equal to 30
# ● nb > 20 and nt > 2 or ng > 30 and nt > 4
# ● Either nb < 60 or ng < 70
# ● Neither nb >= 60 nor ng >= 70
# ● nb is 10 more students than ng
# ● Difference between nb and ng is more than 10 or nt > 5
# ● Either nb is 10 more students than ng or ng is 15 more students than nb

nb, ng, nt = map(input().split())

print(nb>25)
print(ng<= 30)
print(nb>20 and nt > 2 or ng > 30 and nt > 4)
print(nb<60 or ng < 70)
print(not nb>=60 and not ng >=70)
print(nb== ng +10)
print(nb-ng>10 or nt>5)
print(nb==ng+10 or ng==nb +15)


# ● For each expression:
# ○ Manually Simplify it step by step to finally be a T or F
# ● T and T and F and T                          F
# ● T and T and F and T or T and T               T
# ● T and T and T and T or T and (T or F)        T
# ● T and T and T or T and (F or (T and (T and T)))          T
# ● T and T or T and F and T or T and T and F or (T and (T or F))    T
# ● T and T or T and F and T or (T and T and F or (T and (T or F)))      T
# ● (T and T or T and F and T or T) and T and F or (T and (T or F))      T
# ● T and T or T and (F and T or T and T) and F or (T and (T or F))      T



