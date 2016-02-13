import socket
import thread

class ChatClient(object):
    def __init__(self, username):
        self._username = username
        self._socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            
    def connect(self, server, port):
        self._socket.connect((server,port))
        print ("connected to server : " + server)
        thread.start_new_thread(self.recieve,());
        self.send_loop()
            
    def send_loop(self):
        while True:
            data = raw_input(self._username + ":")
            self._socket.sendall(self._username + ":" + data)
            
    def recieve(self):
        while True:
            data = self._socket.recv(1024)
            if data:
                print("\n" + data)
            
class ChatServer(object):
    def __init__(self, username):
        self._socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self._username = username
                    
    def start_server(self, port):
        self._socket.bind( ('',port) )
        self._socket.listen(1)
        print ("started server and listening ... ")
        conn, addr = self._socket.accept() 
        print "connected by " + addr[0]
        self._client = conn
        thread.start_new_thread(self.recieve,());
        self.send_loop()

    def recieve(self):
        while True:
            data = self._client.recv(1024)
            if data:
                print("\n" + data)

    def send_loop(self):
        while True:
            data = raw_input(self._username + ":")
            self._client.sendall(self._username + ":"+ data)