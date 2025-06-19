file_handler = open('MyData.txt', 'r')
str1 = file_handler.read(6)
print(str1)
str1 = file_handler.read(10)
print(str1)
file_handler.close()

# print(type(str1))