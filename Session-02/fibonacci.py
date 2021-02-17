fibonacci = [0,1,1]
a = 1
b = 1
for i in range(1,9):
    c = a + b
    fibonacci.append(c)
    a = b
    b = c
print('The first 11 fibonacci numbers are: ', fibonacci)

