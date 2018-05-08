'''
Date: 20180507
File: s_server.py
Describe: Servidor resposavel receber as conexoes dos
          clientes via socket. Não foi implemetando condição
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
#host e porta
link = (host, port)
#Retorna o horario
time = strftime('%H:%M:%S')

#Carrega a funcao principal do app
if __name__ == '__main__':
    # Cria uma conexao socket do tipo  TCP(SOCK_STREAM) / IPV4 (AF_INET)
    srv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #Bind do ip e porta
    srv_socket.bind(link)
    #Numero maximo de conexao simutanea
    srv_socket.listen(5)
    #Manipulacao (SOL_SOCKET) e Reutilizacao(SO_REUSEADDR)
    srv_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    while 1:
       #Mostra a mensagem ao ser iniciado o servidor
       print('Aguardando conexao...')
       #Socket com a conexao aceita
       client_sock, addr = srv_socket.accept()
       #Mostra o horario em que o cliente fez a conexao
       print('['+ time +' CLIENTE ] conectado --> ', addr)

       #Enquanto estiver conectado = True ou 1
       while 1:
           #Dados recebidos do cliente
           data = client_sock.recv(buffer)
           #Caso nao exista dados ou o decode nao seja utf-8
           #O processo sera encerrado
           if not data or not data.decode('utf-8'): 
               break
           #Mostra o horario que a mensagem foi recebida pelo servidor
           print("["+ time +" CLIENTE] mensagem recebida: %s "  %data.decode('utf-8'))

       #Fecha conexao do cliente
       client_sock.close()
#Encerra o socket servidor
server_socket.close()
