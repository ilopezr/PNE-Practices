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

def fibosum(fibonacci, e):
    suma = 0
    for i in fibonacci[:e]:
        suma += i
    return suma

fibonacci = fibon(n)
suma = fibosum(fibonacci, e)
print('SUM OF THE FIRST 5 TERMS OF FIBONACCI SERIES: ', fibosum(fibonacci, 5))
print('SUM OF THE FIRST 10 TERMS OF FIBONACCI SERIES: ', fibosum(fibonacci, 10) )


