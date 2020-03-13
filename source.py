import socket

my_sock = socket.socket()
my_sock.bind(('', 9090))
my_sock.listen(1)

print("TCPserver listening")

while True:
    try:
        conn, addr = my_sock.accept()
    except:
        pass
    else:
        print("Connected :", addr[0])
        try:
            conn.send("Hi!")
        except:
            print("Disconnected :", addr[0])
conn.close()