#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import socketserver
import sys

if len(sys.argv) != 4:
    sys.exit('Usage: python server.py IP port audio_file')

try:
    IP_SERV = sys.argv[1]
    PORT_SERV = int(sys.argv[2])
    FICHERO= sys.rgv[3]

class EchoHandler(socketserver.DatagramRequestHandler):
    """
    Echo server class
    """

    metodo = line.decode('utf-8').split(' ')[0]
    METODOS = ['INVITE','BYE','ACK']
    def handle(self):
        # Escribe dirección y puerto del cliente (de tupla client_address)
        self.wfile.write(b"Hemos recibido tu peticion")
        while 1:
            # Leyendo línea a línea lo que nos envía el cliente
            line = self.rfile.read()
            print("El cliente nos manda " + line.decode('utf-8'))

            # Si no hay más líneas salimos del bucle infinito
            if not line:
                break
            if not metodo in METODOS:
                self.wfile.write(b'SIP/2.0 405 Method Not Allowed \r\n\r\n')
            elif metodo = 'INVITE':
                send = b'SIP/2.0 100 Trying\r\n\r\nSIP/2.0 100 Trying\r\n\r\n'+
                      +b'SIP/2.0 100 Trying\r\n\r\n'
                self.wfile.write(send)
            elif metodo = 'ACK':
                Ejecuta = 'mp32rtp -i 127.0.0.1 -p 23032 < ' + FICHERO
                print('Vamos a ejecutar', Ejecuta)
                os.systema(Ejecuta)
            elif metodo = 'BYE':
            else:
                self.wfile.write(b'SIP/2.0 400 Bad request\r\n\r\n')

if __name__ == "__main__":
    #Lanzamos un servidor SIP
    serv = socketserver.UDPServer((IP_SERV, PORT_SERV), EchoHandler)
    print('Listening...')
    serv.serve_forever()
