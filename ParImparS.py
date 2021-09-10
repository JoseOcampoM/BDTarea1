def calcularParImpar():
    numero = int(input("ingresa un numero "))

    if numero%2==0:
        print(f"El numero {numero} es par")
    else:
        print(f"El numero {numero} es impar")


def main():
    calcularParImpar()

if __name__=="__main__":
    main()