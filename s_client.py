'''
Date: 20180507
File: s_client.py
Describe: Cliente resposavel pela conexao via socket
          com o servidor. Não foi implemetando condição
          de para, o proposito do codigo é entender a
          comunicao basica via socket.
'''

#Pacote socket
import socket
#Pacote time
from time import strftime, gmtime

#IP do servidor
host = '10.0.0.30'
#Porta de comunicacao do servidor
port = 50000
#Tamanho do buffer
buffer = 1024

#Carrega a funcao principal do app
if __name__ == '__main__':

   #Cria uma conexao socket do tipo  TCP(SOCK_STREAM) / IPV4 (AF_INET)
   client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   #Dados do bind
   sock_addr = (host, int(port))
   #Conectando no servidor
   client_sock.connect(sock_addr)
   #Mensagem default de envio
   payload = 'Hello wordl!'

   #Tratamento de erro
   try:
       #Enquanto estiver conectado = True ou 1
       while 1:
           #Encode UTF-8 da mensagem
           #Necessario para envio da messagem
           client_sock.send(payload.encode('utf-8'))
           #Dados recebidos do servidor
           data = client_sock.recv(buffer)
           #Mostra as mensgens do servidor
           print('Mensagen recebida', data)
   except socket_error as err:
        print("Erro durante a comunicacao %s " % err)

#Fecha a conexao do cliente
client_sock.close()