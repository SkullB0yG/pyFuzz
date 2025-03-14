#!/usr/bin/python


import requests
from requests.exceptions import ConnectionError
import sys
from colorama import Fore, Style, init

init(autoreset=True)

'''Esta funcion se encarga de recorrer un archivo y devolver las palabras
sin saltos de lineas ni espacios'''


def Librarian(path):

    fuzz=[]

    try:
        with open(path, 'r') as file:
            words=file.readlines()

            for word in words:
                unformat=word.strip() 
                fuzz.append(f'/{unformat}')   
            return(fuzz)

    except FileNotFoundError as fileerror:
        print(f'Error: {fileerror}')
    except IsADirectoryError as directoryerror:
        print(f'Error: {directoryerror}')
    except PermissionError as permissionerror:
        print(f'Error: {permissionerror}')
    


'''Esta funcion se encarga de unir la informacion que devuelve la funcion Librerian() y combinarla con una extencionque ingrese el usuario atraves de un parametro y devuelve una lista'''

def ExtensionHandler(url, dictionary, exe):
    
    filewithexe=[]
    try:
        if exe == False:
            for word in dictionary:
               formating = f'{url}{word}'
               filewithexe.append(formating)
            return filewithexe
        else:

            for word in dictionary:
                for e in exe:
                    formating = f'{url}{word}{e}'
                    filewithexe.append(formating)
            return filewithexe
    except NoneType as n:
        print(f'Error: {n}')


def help():
    print(Style.BRIGHT + Fore.CYAN + 'Created by SkullB0yG')
    print('pyFuzz <url> <wordlist> <exetesion>')
    print('''EXAMPLE: 
                    pyFuzz.py http://www.example.com /usr/share/wordlist/rockyou.txt  .py
                    pyFuzz.py http://127.0.0.1 /usr/share/wordlist/rockyou.txt''')


try:

    if sys.argv[1] == '-h'or sys.argv[1] == '--help':
        help()
    elif len(sys.argv[1]) > 0 and len(sys.argv[2]) > 0 and len(sys.argv[3:]) > 0:

        
        # funcion que haga algo con el parametros --url --wordlist --exetesion
        
        urlquery=ExtensionHandler(url=sys.argv[1], dictionary=Librarian( path=sys.argv[2]), exe=sys.argv[3:])
        for url in urlquery:
            response=requests.get(url, timeout=5, allow_redirects = False)
            output=f'{url} ==> (Status Code: {response.status_code})'

            if response.status_code == 404:
                pass
            else:

                if response.status_code in range(301,304) or response.status_code == 403: 
                    print(Fore.YELLOW + output)
                else:
                    print(Fore.GREEN + output) 
    else:

        # funcion que haga algo con el parametros --url --wordlist

        urlquery=ExtensionHandler(url=sys.argv[1], dictionary=Librarian( path=sys.argv[2]), exe=False)

        for url in urlquery:
            response=requests.get(url, timeout=5, allow_redirects = False)
            output=f'{url} ==> (Status Code: {response.status_code})'

            if response.status_code == 404:
                pass
            else:

                if response.status_code in range(301, 304) or response.status_code == 403:
                    print(Fore.YELLOW + output)
                else:

                    print(Fore.GREEN + output)
except ConnectionError:

    stderr=f'[!] server connection error'
    print(Back.RED + stderr)

except KeyboardInterrupt:

    exitout=f'exit'
    print('\n',Style.BRIGHT + Fore.RED + exitout)
