#! /usr/bin/python3
# -*- coding: utf-8 -*-

import zlib
import os
import base64
import threading
from multiprocessing import Process

import time
import sys
import pickle
import zipfile
import logging
import socket
import subprocess
import datetime

try:
    import requests
except:
    print('estamos instalando el modulo requests, por favor espere')
    print(subprocess.getstatusoutput('pip3 install requests')[1])
    print(subprocess.getstatusoutput('pip install requests')[1])
    import requests
try:
    from instabot import Bot
except:
    print('estamos instalando el modulo instabot, por favor espere')
    print(subprocess.getstatusoutput('pip3 install instabot')[1])
    print(subprocess.getstatusoutput('pip install instabot')[1])
    from instabot import Bot
try:
    from http.server import BaseHTTPRequestHandler, HTTPServer
except:
    print('estamos instalando el modulo http, por favor espere')
    print(subprocess.getstatusoutput('pip3 install http')[1])
    print(subprocess.getstatusoutput('pip install http')[1])
    from http.server import BaseHTTPRequestHandler, HTTPServer


from sys import argv
from socket import gethostbyaddr

__VERSION__ = "1.0"
__AUTOR__ = "\033[0;36m           〇├ℳ⅀៘※⃫៙※ጠതШ┗┛┏┓┗┛DESMON┗┛┏┓┗┛Шതጠ※៙※៘⅀ℳ┤〇\033[1;37m"

ipEstatic = subprocess.getstatusoutput(
    "GET http://www.vermiip.es/  | grep 'Tu IP p&uacute;blica es' | cut -d ':' -f2 | cut -d '<' -f1")[1]

print('para ayuda pon el comando: help')

def banner():
    if sys.platform == 'linux' or sys.platform == 'linux2' or sys.platform == 'mac':
        os.system('clear')
    elif sys.platform == 'win32':
        os.system('cls')
    else:
        os.system('clear')

    print("""
	\033[1;31m░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
	\033[1;31m░░\033[1;32m░█▄█░█▀▀░▀█▀░█▀▀░█▀▄░█▀█░█▀▄░█▀▀░▀█▀░█▀▀░█▀▄\033[1;31m░░
	\033[1;31m░░\033[1;32m░█░█░█▀▀░░█░░█▀▀░█▀▄░█▀▀░█▀▄░█▀▀░░█░░█▀▀░█▀▄\033[1;31m░░
	\033[1;31m░░\033[1;32m░▀░▀░▀▀▀░░▀░░▀▀▀░▀░▀░▀░░░▀░▀░▀▀▀░░▀░░▀▀▀░▀░▀\033[1;31m░░
	\033[1;31m░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\033[1;37m"""+"\n"+__AUTOR__)


def MetadataZip(file):
    try:
        zf = zipfile.ZipFile(str(file), "r")

        for info in zf.infolist():
            print(info.filename)
            print("  Comment: " + str(info.comment))
            print("  Modified: " + str(datetime.datetime(*info.date_time)))
            print("  System: " + str(info.create_system) +" (0=MS-DOS OS-2, 3=Unix)")
            print("  ZIP version: " + str(info.create_version))
            print("  Compressed: " + str(info.compress_size) + " bytes")
            print("  Uncompressed: " + str(info.file_size) + " bytes")
        zf.close()

    except FileNotFoundError:
        print('este archivo no esiste, asegurate de introducirlo bien.')


def follower(user, contrasena, user_objetivo):
    for i in range(0, 101):
        mi_bot = Bot()
        mi_bot.login(username=str(user), password=str(contrasena))
        mi_bot.follow_followers(user_objetivo)


def CodingBase85Text(text):
    data = base64.b85encode(text.encode('utf-8'), pad=False)
    print('salida:\033[1;32m   '+str(data.decode())+"\033[1;37m")


def DecodingBase85Text(text):
    data = base64.b85decode(text.encode())
    print('salida:\033[1;32m   '+str(data)+"\033[1;37m")


def CodingBase85File(text):
    data = base64.b85encode(text.encode('utf-8'), pad=False)
    file = open("archivo_encriptado85", "w")
    file.write(data.decode())
    file.close()


def DecodingBase85File(text):
    data = base64.b85decode(text.encode('utf-8'))
    file = open("archivo_desencriptado85", "w")
    file.write(data.decode())
    file.close()


def EncriptBinary(text):
    file = open(str(text), "r")
    file_bin = open('archivo_binario', "wb")
    text = file.read()
    pickle.dump(str(text), file_bin)
    file_bin.close()
    file.close()


def DecodingBinary(file):
    fichero = open(str(file), "rb")
    dataOput = pickle.load(fichero)
    fichero.close()
    fichero = open("archivo_desencriptado.txt", "w")
    fichero.write(str(dataOput))
    fichero.close()
    print('salida:\033[1;32m   '+dataOput+"\033[1;37m")


def YourDataInfo(ipEstatic):
    print("\n\n\a\ntu ip estatica o publica es: " + str(ipEstatic))
    print("tu sistema operativo(OS) es: " + str(sys.platform))
    print("tiempo: " + str(datetime.date.today()))
    print('directorio: ' + str(os.getcwd()))
    print("nombre del equipo: " + str(socket.gethostname()))
    print("tu ip_v4 es: " + str(socket.gethostbyname(socket.gethostname()))+"\n\n\a")


def nmapDemoTcp(host, MiniPort, MaxPort):

    # host = '192.168.1.1'
    # MaxPort = 54  # puerto por el que se empieza a escanear
    # MiniPort = 1  # puerto maximo a escanear
    number = 1  # el numero de conexiones que lleva creadas

    OpenPort = []
    esitenNetwork = []

    try:
        while True:

            if MiniPort < MaxPort and 65536 >= MaxPort:

                try:
                    #time.sleep(0.04)

                    sock = socket.socket(
                        socket.AF_INET, socket.SOCK_STREAM, proto=0, fileno=None)
                    # empieza a escanear por el puerto escaneado

                    sock.connect((str(host), int(MiniPort)))
                    # muestra si la conecsion fue establecida

                    print('conexion establecida,' + str(host) + ':' +
                        str(MiniPort) + ' el puerto: ' + str(MiniPort))

                    sock.close()
                    OpenPort.append(MiniPort)
                    number = number + 1
                    esitenNetwork.append(host+":"+str(MiniPort))

                    # print(OpenPort)

                except ConnectionRefusedError:

                    print('El puerto: ' + str(MiniPort) + ' no esta abierto')

                MiniPort = MiniPort + 1

            else:

                print('Escaneo completo')
                print(str(esitenNetwork))
                break
    except KeyboardInterrupt:
        print(str(esitenNetwork))


def conect(ip):

    print('\n\n\n')
    url = 'http://' + str(ip) + '/'
    p = requests.get(url, stream=True)
    print('contenido Html: \n'+str(p.content))
    print(p.cookies)
    print(p.encoding)      # returns 'utf-8'
    print(p.status_code)   # returns 200
    print(p.elapsed)      # returns datetime.timedelta(0, 1, 666890)
    print(p.url)           # returns 'https://tutsplus.com/'
    print(p.history)
    file = open('pagina_web.html', 'w')
    file.write(str(p.content))
    file.close()


def scannNetwork(IpMinima, IpMaxima):

    if int(IpMaxima) == 1:
        IpMaxima += 1
        
    def scan(addr, port):
        #creates a new socket using the given address family. 
        socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        #setting up the default timeout in seconds for new socket object 
        socket.setdefaulttimeout(0.1)

        #returns 0 if connection succeeds else raises error 
        result = socket_obj.connect_ex((addr,port)) #address and port in the tuple format 

        #closes te object 
        socket_obj.close()

        return result

    # lista de puertos a escanear
    
    def start():
        try:

            ports=[1, 5, 7, 9, 11, 13, 17, 18, 19, 20, 21, 22, 23, 25, 42, 43, 53, 63, 66, 80, 115, 139, 443, 591, 445, 1080, 1234, 6969, 8080, 8000, 42004] # puertos mas usados a escanear.
                    
            existenNetwork=list()
            # bucle por todas las ip del rango 192.168.1.*
            for i in range(int(IpMinima),int(IpMaxima)):
                addr="192.168.1.{}".format(i)
                for port in ports:
                    result=scan(addr, port)
                    if result==0:
                        print(addr, port, "\033[1;32mAbierto\033[1;37m")
                        existenNetwork.append((str(addr), str(port)))

                    else:
                        print(addr, port, "\033[1;31mCerrado\033[1;37m")
            os.system('clear')
            print('\033[1;32respuesta en crudo: '+str(existenNetwork)+"\033[1;37")
            
        except KeyboardInterrupt:
            os.system('clear')
            print('\033[1;32respuesta en crudo: '+str(existenNetwork)+"\033[1;37")
            
    start()

def serverHtpp(hosts, port, data, ipEstatic):
    try:
        print("\n\n\n\nserver abierto en el host: " + str(hosts) + "\npor el puerto: " + str(port) + "\n\a url para ti: http://" +
              str(hosts) + ":" + str(port)+"//\nruta para la vitima: http://"+str(ipEstatic)+":"+str(port)+"/")
        print('Servidor iniciado, usa <Ctrl-C> para parar el servidor.\n')
        try:
            file = open(str(data), "r")
            data = file.read()
            file.close()
        except FileNotFoundError:
            print('no se pudo abrir el archivo por que no existe.')
        print('el contenido de tu archivo es: \n'+data)

        class S(BaseHTTPRequestHandler):
            def _set_response(self):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

            def do_GET(self):
                logging.info("Solicitud GET,\nPath: %s\nHeaders:\n%s\n", str(
                    self.path), str(self.headers))
                self._set_response()
                self.wfile.write(str(data).format(self.path).encode('utf-8'))

            def do_POST(self):
                # <--- Gets the size of data
                content_length = int(self.headers['Content-Length'])
                # <--- Gets the data itself
                post_data = self.rfile.read(content_length)
                logging.info("solicitud POST,\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n", str(
                    self.path), str(self.headers), post_data.decode('utf-8'))
                self._set_response()
                self.wfile.write("Solicitud POST para {}".format(
                    self.path).encode('utf-8'))
        try:
            def run(hosts, port, server_class=HTTPServer, handler_class=S):
                logging.basicConfig(level=logging.INFO)
                server_address = (str(hosts), int(port))
                httpd = server_class(server_address, handler_class)
                logging.info('Iniciando server Http...\n')
                try:
                    httpd.serve_forever()
                except:
                    httpd.server_close()
                logging.info('Stopping httpd...\n')

                # server.serve_forever()
        except:
            print('server cerrado.')
        hilo1 = threading.Thread(target=run(hosts, port))
        hilo1.setDaemon(True)
        hilo1.start()
        banner()

    except KeyboardInterrupt:
        http.server_close()
        banner()
        print("server finalizado")


YourDataInfo(ipEstatic)


if __name__ == '__main__':
    
    while True:
        banner()
        opcion = str(input(">>: "))
        if opcion == '1':
            file = str(input('archivo al que obtener metadatos: '))
            MetadataZip(file)
            file = None
        elif opcion == '2':
            user = str(input('tu cuenta de instagram: '))
            contrasena = str(input('tu contrasena: '))
            user_objetivo = str(input('usuario al que subir 100 seguidores: '))
            follower(user, contrasena, user_objetivo)
            user = None
            contrasena = None
            contrasena = None

        elif opcion == '3':
            text = str(input('texto a codificar en base85: '))
            CodingBase85Text(text)
            text = None

        elif opcion == '4':
            text = str(input('texto a descodificar en base85: '))
            DecodingBase85Text(text)
            text = None

        elif opcion == '5':
            text = str(input('archivo a codificar en base85: '))
            CodingBase85File(text)
            text = None

        elif opcion == '6':
            text = str(input('archivo a descodificar en base85: '))
            DecodingBase85File(text)
            text = None

        elif opcion == '7':
            text = str(input('archivo a codificar en binario: '))
            file = open(str(text), 'r')
            text = file.read()
            file.close()
            EncriptBinary(text)
            text = None

        elif opcion == '8':
            file = str(input('archivo a descodificar en binario: '))
            DecodingBinary(file)
            file = None

        elif opcion == '9':
            YourDataInfo(ipEstatic)
            print('esta es tu info')

        elif opcion == '10':
            # str(input())
            host = str(input('ip a la que escanear sus puertos: '))
            MiniPort = int(input('puerto por el que empezar a escanear: '))
            MaxPort = int(input('puerto maximo a escanear(maximo existente 65535): '))
            nmapDemoTcp(host, MiniPort, MaxPort)

        elif opcion == '11':
            ip = str(input('ip o url a la que hacer peticion get: '))
            conect(ip)

        elif opcion == '12':
            IpMinima = str(input('ultimo numero de la ip por la que empezar a escanear(para toda la red 1): '))
            IpMaxima = int(input('ultimo numero de la ip por la que acabar de escanear(para toda la red 255): '))
            scannNetwork(IpMinima, IpMaxima)

        elif opcion == '13':
            port = str(input('puerto en el que abrir el server: '))
            data = str(input('archivo con contenido html, php, css, o javascript que usar: '))
            serverHtpp('127.0.0.1', port, data, ipEstatic)
            data = None
            port = None

        elif opcion == 'help' or opcion == '14':
            print("""
\topciones:             usos
\t
\t   1 \tobtencion de metadatos de archivos .zip\n
\t   2 \t      seguidores de intagram.\n
\t   3 \t     codificar texto en base85\n
\t   4 \t    descodificar texto en base85\n
\t   5 \t    codificar archivos en base85\n
\t   6 \t   descodificar archivos en base85\n
\t   7 \t    codificar archivos en binario\n
\t   8 \t   descodificar archivos en binario\n
\t   9 \t           tu informacion\n
\t   10\t     escaner de puertos individual\n
\t   11\t  peticion get de tipo http a una ip o url(scraping)\n
\t   12\tescaner de hosts con el uso de un solo puerto\n
\t   13\t  server http, para phising y otros usos\n
\t   14\t                ayuda\n
\t   15\t                salir\n
				""")

        elif opcion == '15':
            break
            sys.exit()
        
            

        elif opcion == 'desmon':
            print('por favor, si tuvo algun problema contacte con migo.')

        else:
            print('introduze una opcion correcta. :(')

        input('\n\a\nEnter por favor...')
    #except KeyboardInterrupt:
    #    print('algo as echo mal. :(')
