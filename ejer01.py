
def carga_keywords():
    list_menu = []
    text =""
    keywords =[]

    with open('keywords.txt') as file:

        for line in file:
            text +=line
            list_menu = text.split()

    
        for kw in list_menu:
            if list_menu.count(kw) > 1:
                keywords.append(kw)
        
        keywords = set(keywords)
    return keywords



# Se verifica si el usuario no ha introducido una opcion correcta
i=True
while i == True:
    # El usuario debera entroducir valores 0,1 ò 2
    option = int(input("Seleccione una Opcion:\n[1] – Importar palabras clave\n[2] – Mostrar palabras clave\n[0] – Salir\n"))
    if option <=0 and option >=2:
        print("Ha introducido una Opcion Incorrecta (1,2 ò 0\n)")
        option = int(input("Seleccione una Opcion:\n[1] – Importar palabras clave\n[2] – Mostrar palabras clave\n[0] – Salir\n"))
    else:
        if option == 1:
            keywords = carga_keywords()
            print ("Cargando Lista de Palabras Clave...")
        elif option == 2:
            keywords = carga_keywords()
            if (len(keywords)) > 20:
                cont = 0
                for i, j in enumerate(keywords,1):
                    if cont <= 19:
                        print (i, j)
                        cont +=1
                    else:
                        stop = input ("Presione cualquier tecla para    continuar")
                        cont = 0
            elif (len(keywords)) < 20:
                for i, j in enumerate(keywords,1):
                    print (i, j)
            i= True
        elif option == 0:
            print("Hasta Pronto")
            i = False