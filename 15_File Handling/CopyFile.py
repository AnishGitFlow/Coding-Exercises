f = open('Python.jpeg', 'rb')
data = f.read()

cp = open('Python2.jpeg', 'wb')

cp.write(data)

f.close()
cp.close()