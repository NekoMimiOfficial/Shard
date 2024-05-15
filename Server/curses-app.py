import common
import socket
import threading

class Server:
    def __init__(self, port = 10039):
        self.port = port
        self.runLock = True
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.Error = common.ErrorEmmiter()

    def start(self):
        self.socket.bind(('localhost', self.port))
        self.socket.listen()
        
        while self.runLock:
            conn, addr = self.socket.accept()
            thread = threading.Thread(target=self.worker, args=[conn])
            thread.start()

    def lexDL(self, connection: socket.socket, pckSize):
        shardURI = connection.recv(pckSize)
        shardURI = shardURI.decode()
        print(*shardURI,)
        self.runLock = False

    def worker(self, connection: socket.socket):
        sockVer, cmd = connection.recv(2)
        print(sockVer)
        print(cmd)

        if not sockVer == 1:
            self.Error.version(connection)

        match cmd:
            case 1:
                pckSize = int.from_bytes(connection.recv(4))
                print(pckSize)
                self.lexDL(connection, pckSize)

server = Server()
server.start()
