def calcular_multiplo(a, b):
    return a % b == 0

def main():
    numero = int(input("Ingrese un numero entero de 4 cifras: "))

    while(numero <= 999 or numero >= 10000):
        numero = int(input("NUMERO NO VALIDO, Ingrese un numero entero de 4 cifras nuevamente: "))

    digitos = [] 

    for i in range(4):
        digitos.append(numero%10)
        numero = int(numero/10)

    if(calcular_multiplo(digitos[3], digitos[0])):
        print("El primer digito es multiplo del cuarto digito\n")
    else:
        print("El primer digito NO es multiplo del cuarto digito\n")

    print(f"La suma del segundo y tercer digito es {digitos[1]+digitos[2]}")


if __name__ == "__main__":
    main()