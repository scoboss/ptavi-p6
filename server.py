#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import socketserver
import sys
import os

if len(sys.argv) != 4:
    sys.exit('Usage: python server.py IP port audio_file')

try:
    IP_SERV = sys.argv[1]
    PORT_SERV = int(sys.argv[2])
    FICHERO = sys.rgv[3]
except Exception:
    sys.exit('Usage: python server.py IP port audio_file')
if not os.path.exists(FICHERO):
    sys.exit('Usage: python server.py IP port audio_file')


class EchoHandler(socketserver.DatagramRequestHandler):

    METODOS = ['INVITE', 'BYE', 'ACK']

    def handle(self):
        while 1:
            # Leyendo línea a línea lo que nos envía el cliente
            line = self.rfile.read()
            if not line:
                break
            metodo = line.decode('utf-8').split(' ')[0]
            if not metodo in self.METODOS:
                self.wfile.write(b'SIP/2.0 405 Method Not Allowed \r\n\r\n')
            elif metodo == 'INVITE':
                send = b'SIP/2.0 100 Trying\r\n\r\n
                send += b'SIP/2.0 180 Ring\r\n\r\n'
                send += b'SIP/2.0 200 OK\r\n\r\n'
                self.wfile.write(send)
            elif metodo = 'ACK':
                Ejecuta = '/mp32rtp -i 127.0.0.1 -p 23032 < ' + FICHERO
                print('Vamos a ejecutar', Ejecuta)
                os.system(Ejecuta)
            elif metodo = 'BYE':
                self.wfile.write(b'SIP/2.0 200 OK\r\n\r\n')
            else:
                self.wfile.write(b'SIP/2.0 400 Bad request\r\n\r\n')

if __name__ == "__main__":
    #Lanzamos un servidor SIP
    serv = socketserver.UDPServer((IP_SERV, PORT_SERV), EchoHandler)
    print('Listening...')
    serv.serve_forever()
