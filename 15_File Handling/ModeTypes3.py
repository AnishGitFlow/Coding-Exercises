file = open('ModeDemo', 'r+')
str1 = file.read(10)
print(str1)

file.write('Good bye!')
file.close()