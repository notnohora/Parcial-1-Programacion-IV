class CifradoCesar:
    def __init__(self, desplazamiento):
        self.desplazamiento = desplazamiento
        self.alfabeto = 'abcdefghijklmnopqrstuvwxyz'

    def cifrar(self, texto):
        texto = texto.lower()
        cifrado = []
        for letra in texto:
            if letra in self.alfabeto:
                idx = self.alfabeto.index(letra)
                nuevo_idx = (idx + self.desplazamiento) % len(self.alfabeto) #el modulo asegura que vuelva al inicio del alfabeto si se pasa el indice
                cifrado.append(self.alfabeto[nuevo_idx])
            else:
                cifrado.append(letra) #caracteres que no estan en el alfabeto
        return ''.join(cifrado)

    def descifrar(self, texto):
        texto = texto.lower()
        descifrado = []
        for letra in texto:
            if letra in self.alfabeto:
                idx = self.alfabeto.index(letra)
                nuevo_idx = (idx - self.desplazamiento) % len(self.alfabeto)
                descifrado.append(self.alfabeto[nuevo_idx])
            else:
                descifrado.append(letra)
        return ''.join(descifrado)

    def guardar_en_archivo(self, texto, nombre_archivo):
        with open(nombre_archivo, 'w') as archivo:
            archivo.write(texto)

    def leer_de_archivo(self, nombre_archivo):
        with open(nombre_archivo, 'r') as archivo:
            return archivo.read()

desplazamiento = int(input("Ingrese el desplazamiento para el cifrado Cesar: "))
cesar = CifradoCesar(desplazamiento)
texto_original = input("Ingrese el texto a cifrar: ")
cifrado = cesar.cifrar(texto_original)
cesar.guardar_en_archivo(cifrado, "cifrado.txt")

texto_leido = cesar.leer_de_archivo("cifrado.txt")
descifrado = cesar.descifrar(texto_leido)

print("Texto original:", texto_original)
print("Texto cifrado:", cifrado)
print("Texto descifrado:", descifrado)
