import socket
import json
from search import Search

def start_server(host='127.0.0.1', port=5001):
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket.bind((host, port))
    serverSocket.listen(1)
    print(f"Server is running at {host}:{port}")

    while True:
        clientSocket, addr = serverSocket.accept()
        print(f"Server Connected to at {addr}")

        data = clientSocket.recv(1024).decode()
        if not data:
            break

        try:
            req = json.loads(data)
            filename = req.get('filename', 'note.txt')
            word = req['word']

            search_f = Search(filename)
            search_f.clean()
            result = search_f.get_lines(word)
            response = json.dumps(result)

        except Exception as e:
            response = json.dumps({"error": str(e)})

        clientSocket.sendall(response.encode())
        clientSocket.close()



if __name__ == "__main__":
    start_server()
