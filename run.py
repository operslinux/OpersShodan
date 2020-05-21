# -*- coding: utf-8 -*-
from form.find import OpcionShoda, Abrirweb
import shodan
import os
from colorama import Back, Fore, init
import sys
from tqdm import tqdm
from time import sleep
from form.logo import LogoTwo, LogoCero, LogoOne

init()
Menus = list(('- SI','- NO','- SALIR','- TODOS LOS DATOS','- SOLO LAS IP', '- [NEW] Servidores FTP vulnerables','- CONTRASEÑAS DEFAULT CAMARAS'))
def Carga():
    loop = tqdm(total=50000, position=0, leave=False)
    for k in range(50000):
        loop.set_description("Loading .....".format(k))
        loop.update(1)
    loop.close()

def MenuInicial():
    os.system('clear')
    LogoCero()
    sleep(0.7)
    os.system('clear')
    sleep(0.3)
    LogoCero()
    sleep(0.3)
    os.system('clear')
    sleep(0.3)
    LogoOne()
    sleep(0.3)
    os.system('clear')
    sleep(0.3)
    LogoCero()
    sleep(1.5)
    sleep(0.60)
    Carga()
    print(Fore.GREEN + "\t\tBienvenido a OPers Shodan BY OPERS LINUX\t\t")
    print("\t\t__________________________\t\t")

#comprobacion verificara que la carpeta exista junto con car,limpiar y animacion
def Comprobacion():
    Carga()
    Animacion()
    print(Fore.WHITE + "Comprobando la EXISTENCIA de la Carpeta Cookies")
    if os.path.isdir('cookies') == True:
        print(Fore.GREEN + "La Carpeta Cookies SI EXISTE")
    else:
        print(Fore.RED + "La Carpeta Cookies NO EXISTE")
        print(Fore.WHITE + "Creando Carpeta.....")
        os.system('mkdir cookies')

def MenuLogin():
    print(Fore.WHITE + "Si tienes ya una API Valida guardada coloca 1 de lo contrario para poner tu API coloca 2")
    for i in range(1,4):
        if i == 1:
            print(Fore.MAGENTA + "\t\t<Menu>\t\t")

            print(i, Menus[0])
        if i == 2:
            print(i, Menus[1])
        if i == 3:
            print(i, Menus[2])



def MenuDatos():
    for i in range(1, 6):
        if i == 1:
            print(Fore.MAGENTA + "\t\t<Menu>\t\t")

            print(i, Menus[3])
        if i == 2:
            print(i, Menus[4])
        if i == 3:
            print(i, Menus[5])
        if i == 4:
            print(i, Menus[2])
        if i == 4:
            print(i, Menus[6])

def main():
    Comprobacion()
    MenuLogin()
    try:
        Lopcion = int(input(Fore.RED + 'Coloca el numero de la opcion a elegir\n [ Opers Linux ] > '))
        if Lopcion == 1:
            print(Fore.WHITE + "Comprobando si Existe API.txt")
            Carga()
            if os.path.isfile('cookies/API.txt') == True:
                print("El Archivo API.txt EXISTE")
                MenuDatos()
                OpcionShoda()

            else:
                Limpiar()
                print(Fore.YELLOW + "El archivo API.txt NO existe")
                main()

        elif Lopcion == 2:
            Ipsho = input(Fore.YELLOW + "Coloca Tu API DE SHODAN\n [ Opers Linux ] > ")
            f = open('cookies/API.txt', 'w')
            f.write(Ipsho)
            print(Fore.WHITE + """TU API HA SIDO GUARDADA CON EXITO SUSTITUIRA LA ANTERIOR EN CASO DE...
            INICIA DE NUEVO PARA CONTINUAR CON TU API YA GUARDADA Y SELECCIONA 1""")
            f.close()

        else:
            LogoTwo()
            print(Fore.RED + "[SALIENDO]")



    except:
        print(Fore.RED + "[Error]", "Debes colocar una Opcion Valida Intenta de nuevo ")
        main()





if __name__ == '__main__':
    main()
