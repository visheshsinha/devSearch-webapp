from socket import *


def createServer():
    serverSocket = socket(AF_INET, SOCK_STREAM)

    try:
        serverSocket.bind(("localhost", 9000))
        serverSocket.listen(5)

        while True:
            (clientSocket, address) = serverSocket.accept()

            # ________below doesn't execute until a request is accepted________

            rd = clientSocket.recv(5000).decode()
            pieces = rd.split("\n")
            if len(pieces) > 0:
                print(pieces[0])

            data = "HTTP/1.1 200 OK\r\n"
            data += "Content-Type: text/html; charset=utf-8\r\n"
            data += "\r\n"
            data += "<html><body>Hello World</body></html>\r\n\r\n"

            clientSocket.sendall(data.encode())
            clientSocket.shutdown(SHUT_WR)

    except KeyboardInterrupt:
        print("\nShutting Down...\n")

    except Exception as exc:
        print("Error:\n")
        print(exc)

    serverSocket.close()


print("Access http://localhost:9000")
createServer()
