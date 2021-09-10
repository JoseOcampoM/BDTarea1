def es_numero_perfecto():
    numero = int(input('Escribe un numero: '))
    contador = 0
    
    for i in range(1, numero):
        if numero % i == 0:
            contador += i

    if contador == numero:
        print('El numero es perfecto')
    else:
        print('El numero no es perfecto')

def main():
    es_numero_perfecto()

if __name__ == '__main__':
    main()