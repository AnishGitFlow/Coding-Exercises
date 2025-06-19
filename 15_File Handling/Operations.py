file = open('prop.txt', 'r')

# line = file.readline()
# print(line, end='')

lines = file.readlines()
# print(line)

# print(file.name)
# print(file.mode)
# print(file.closed)

for line in lines:
    print(line, end='')