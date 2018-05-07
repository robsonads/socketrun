'''
Cliente socket
'''

import socket
from time import strftime, gmtime

#IP do servidor
host = '10.0.0.30'
#Porta de comunicacao do servidor
port = 50000
#Tamanho do buffer
buffer = 256

#Carrega a funcao principal da app
if __name__ == '__main__':

   #Cria uma conexao do TCP
   client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   #Dados do bind
   sock_addr = (host, int(port))
   #Conectando no servidor
   client_sock.connect(sock_addr)
   #Mensagem default para envio
   payload = 'Hello wordl!'

   #Tratamento de erro
   try:
       while 1: #Enquanto estiver conectado
           #Decodifica e enviar mensagem para o servido
           client_sock.send(payload.encode('utf-8'))
           #Recebe mensagem do servidor
           data = client_sock.recv(buffer)
           #Mostra as mensgens do servidor
           print('Mensagen recebida', data)
   except socket_error as err:
        print("Erro durante a comunicacao. %s " % err)

#Fecha a conexao do cliente
client_sock.close()