line = "apple,banana, , , apple,student### #student$$apple"

new_line = sorted(line.replace(',', ' ').replace('$', ' ').replace('#', ' ').split())

print(new_line)
 