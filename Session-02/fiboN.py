def fibon(n):
    fibonacci = [0, 1, 1]
    a = 1
    b = 1
    for i in range(1, n-2):
        c = a + b
        fibonacci.append(c)
        a = b
        b = c
    return fibonacci

try:
    n = int(input('Enter here an integer number: '))
    fibonacci = fibon(n)
    print('The 5th fibonacci term: ', fibonacci[5])
    print('The 10th fibonacci term: ', fibonacci[10])
    print('The 15th fibonacci term: ', fibonacci[15])
except ValueError:
    print('The value you have introduced is not an integer number.')