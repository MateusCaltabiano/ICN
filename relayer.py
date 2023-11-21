import socket

buffer_size = 1024
relayer_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

relayer_socket.bind(('240.10.11.12', 5000))
client_port = 0

while True:
  data, address_and_port = relayer_socket.recvfrom(buffer_size)
  if(address_and_port[0] == '240.5.6.7'):
    client_port = address_and_port[1]
    relayer_socket.sendto(data, ('240.15.16.17', 30000))
  else:
    relayer_socket.sendto(data, ('240.5.6.7', client_port))
