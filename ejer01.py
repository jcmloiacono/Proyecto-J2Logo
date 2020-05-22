import requests
from bs4 import BeautifulSoup
from lxml import etree


''' LISTA DE VARIABLES UTILIZADAS
    list_menu    (Variable del a funcion Cargar_keywords)
    text         (Variable del a funcion Cargar_keywords)
    keywords     (Variable del a funcion Cargar_keywords)
    option       (Variable de inicio de programa para seleccionar opcion)
    kw           (Palabra Clave que Introducira el usuario, sirve para introducir y buscar)
    dominio      (Dominio donde el usuario desea buscar la informacion)
    position     (Devolvera el resultado del posicionamiento en el dominio)
    url          (Variable de la funcion Compueba_Keywords)
    resp         (Response del request)
    stop         (Variable solo para darle continuidad al mostrar por pantalla la lista mayor a 20)

'''
def carga_keywords(kw):

    with open('keywords.txt', 'a+') as file:
        file.writelines("\n"+"\n{}".format(kw))
    
def mostrar_keywords():
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

def comprueba_keywords(kw, dominio):
    
    url = 'https://www.google.com/search?q={}&start=start'.format(kw)
    response = requests.get(url)
    
    #Verifico si la conexion esta activa, osea =200
    if response.status_code != 200:
        print ("Ha ocurrido un error con la conexion!!")
    else:
        print ("Conexion establecida...")
        
        soup = BeautifulSoup(response.text, 'html.parser')
        data = soup.find_all('div', class_='kCrYT')
        cont = 1
        for d in data:
            if dominio not in str(d):
                cont+=1
            else:
                return cont
       

def menu(option):
    if option == "1":
        kw = input("Introduzca la palabra clave que desea agregar: ")
        keywords = carga_keywords(kw)
        print ("Se ha cargado la palabra clave...")
                
    elif option == "2":
        keywords = mostrar_keywords()
        if (len(keywords)) > 20: # En caso de que la lista sea mayor a 20 palabras claves
            cont = 0
            for i, j in enumerate(keywords,1):
                if cont <= 19:
                    print (i, j)
                    cont +=1
                else:
                    stop = input ("Presione cualquier tecla para continuar")
                cont = 0
        elif (len(keywords)) < 20: # En caso de que la lista sea menor a 20 palabras claves
            for i, j in enumerate(keywords,1):
                print (i, j)

                
    elif option =="3":
        kw = input("Introduzca la palabra clave que desea buscar: ")
        dominio = input("Introduzca el sitio web donde desea Buscar: ")
        position = comprueba_keywords(kw, dominio)
        if  position == None or position >= 100:
            print ("La palabra clave {} para el dominio {} se encuentra en la posicion {}\n".format(kw,dominio, "+100"))
        else:
            print ("La palabra clave {} para el dominio {} se encuentra en la posicion {}\n".format(kw,dominio, position))
            


    # Se verifica si el usuario no ha introducido una opcion correcta

if __name__ == "__main__":
    i=True
    while i == True:
        
        print("")
        print("")
        print( "          **  ***   *******  **    **")
        print( "          **  **    **        **  **")
        print( "          ** **     *****       **")
        print( "          **  **    **          **")
        print( "          **  ****  *******     **")
        print("")
        print("")
        print( "**       **  *********  *******   ********    *********")
        print( "**       **  **     **  **    **  **     **   **")
        print( "**   **  **  **     **  ******    **      **  *********")
        print( "**   **  **  **     **  **   **   **     **           **")
        print( "***********  *********  **     ** *******     **********")
        
        # El usuario debera entroducir valores 0,1,2 ò 3
        option = input("\nSeleccione una Opcion:\n [1] – Importar palabras clave\n [2] – Mostrar palabras clave\n [3] - Comprobar palabras clave\n [0] – Salir\n")
        if option.isdigit() == False or option <"0" or option >="4":
            print ("\033[31;48m","No introdujo una opcion valida")
            print ("\033[0;0m")
        elif option == "0":
            print("Hasta Pronto!!\n")
        
            i = False
        else:
            menu(option)


