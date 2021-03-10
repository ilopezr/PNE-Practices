def sumn(n):
    res = 0
    for i in range(1, n + 1):
        res += i
    return res

print('Sum of the first 20 integers : ', sumn(20))
print('Sum of the first 100 integers : ', sumn(100))

#Cuando usamos el step over, se empieza a revisar desde un punto hacia abajo
#Cuando usamos el step into, se empieza a revisar desde un punto escogido, ttodo lo de arriba, y cuando se termina,
#se empieza a revisar lo de debajo. SOLO SE USA PARA INTRODUCIRSE EN FUNCIONES
