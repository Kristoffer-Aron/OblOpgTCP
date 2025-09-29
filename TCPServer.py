from socket import *
import threading
import random

def service(socket):
  while True:
    command = socket.recv(1024).decode().strip()
    
    if not command:  # Client disconnected
            break
    print('Received:', command)
    socket.send("Input Numbers\n".encode())
    numbers = socket.recv(1024).decode()
    numbersSplit = numbers.split(" ", 1)
    print('Received Numbers:', numbers)
    
    if command == "Random":
      randNum = random.randint(int(numbersSplit[0]), int(numbersSplit[1]))
      socket.send(f"{randNum}\n".encode())
      print('Sent Random Number:', randNum)
      
    if command == "Add":
      sumNum = int(numbersSplit[0]) + int(numbersSplit[1])
      socket.send(f"{sumNum}\n".encode())
      print('Sent Sum:', sumNum)
      
    if command == "Subtract":
      subNum = int(numbersSplit[0]) - int(numbersSplit[1])
      socket.send(f"{subNum}\n".encode())
      print('Sent Subtraction:', subNum)


serverport = 12345
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverport))
serverSocket.listen(2)
print('The server is ready to receive')
while True:
  connectionSocket, addr = serverSocket.accept()
  #connectionSocket.settimeout(20)
  print('Connection from:', addr)
  
  try:
    # Use threading to handle multiple clients
    threading.Thread(target=service, args=(connectionSocket,)).start()
    #service(connectionSocket)
  
  except timeout:
    print('Socket timed out, closing connection')
    connectionSocket.close()