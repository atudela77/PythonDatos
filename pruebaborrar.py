def prueba(*var: int):
    ''' Esto es una función que prueba el empaquetado de datos.
    Lo que hace es:
        1. Recibe una serie de números separados por comas.
    '''
    return sum(var)


def diccpack(**var):
    return var


def posnom(a, b, c, /, *, d):
    return a + b - c - d


def main():
    cakir = (1, 2, 3, 4, 5, 6, 7, 8)
    print(prueba(1, 2, 3, 4, 5, 6, 7, 8))
    print(prueba(2.3, 3.4))
    print(prueba(*cakir))
    diccion = diccpack(edad=23, nombre="Antonio", direccion="calle")
    otro = diccpack(**diccion)
    print(otro)
    print(posnom(1, 2, 3, d=4))
    

main()
