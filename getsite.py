import socket

mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

mysocket.connect(('www.facebook.com', 443))
mysocket1.connect(('www.twitter.com', 443))

cmd  = 'GET https://www.facebook.com/BentongX?ref=bookmarks HTTPS/1.0\n\n\n\n'.encode()
cmd1  = 'GET https://twitter.com/i/flow/signup HTTPS/1.0\n\n\n\n'.encode()

mysocket.send(cmd)
mysocket1.send(cmd1)

while True:
    data = mysocket.recv(1000)
    data1 = mysocket1.recv(1000)

    if(len(data) < 1):
        break
    if(len(data1) < 1):
        break

    print (data.decode())
    print (data1.decode())

mysocket.close()
mysocket1.close()
