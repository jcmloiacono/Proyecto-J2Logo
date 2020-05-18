
def carga_keywords():
    keywords = []

    with open('keywords.txt') as file:

        for line in file:
            if line not in keywords:
                keywords.append(line[:len(line)-1])

    return keywords

# El usuario debera entroducir valores 0,1 ò 2
option = int(input("Seleccione una Opcion:\n[1] – Importar palabras clave\n[2] – Mostrar palabras clave\n[0] – Salir\n"))

# Se verifica si el usuario no ha introducido una opcion correcta
i=True
while i == True:
    if option >=0 and option <=2:
        i = False
    else:
        print("Ha introducido una Opcion Incorrecta (1,2 ò 0\n)")
        option = int(input("Seleccione una Opcion:\n[1] – Importar palabras clave\n[2] – Mostrar palabras clave\n[0] – Salir\n"))

if option == 1:
    keywords = carga_keywords()
    print (keywords)
elif option == 2:
    keywords = carga_keywords()
    if (len(keywords)) > 20:
        cont = 0
        for i, j in enumerate(keywords,1):
            if cont <= 19:
                print (i, j)
                cont +=1
            else:
                stop = input ("Presione cualquier tecla para continuar")
                cont = 0
    else:
        for i, j in enumerate(keywords,1):
            print (i, j)