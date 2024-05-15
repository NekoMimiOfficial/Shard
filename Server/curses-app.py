import socket
import common
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

    def downloadResolver(self, connection: socket.socket, job, id, issue):
        pass

    def lexDL(self, connection: socket.socket, pckSize):
        packet = connection.recv(pckSize)
        shardURI = packet.decode()

        # oh boi dis lixer gorjus
        # i literlly just came up with it in 2 mins
        buffer = ''
        com = ''
        ident = 0
        for char in shardURI:
            if not char == ':':
                if ident > 0:
                    com += char
                buffer += char
            else:
                ident += 1

        synType = ('reserved', 'child', 'object')
        return self.downloadResolver(connection, synType[ident], buffer, com)
        
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
                dlObjHandle = self.lexDL(connection, pckSize)

server = Server()
server.start()
