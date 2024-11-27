import socket
import json

def client_request(filename, word, host='127.0.0.1', port=5001):

    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect((host, port))

    request = json.dumps({"filename": filename, "word": word})
    clientSocket.sendall(request.encode())

    response = clientSocket.recv(1024).decode()
    clientSocket.close()

    result = json.loads(response)
    if "error" in result:
        print(f"Error: {result['error']}")
    else:
        print("Search Results:")
        for item in result[1:]:
            print(f"Line {item[0]}: {item[1]}")

if __name__ == "__main__":
    filename = input("Enter the filename (Or leave it as  default): ") or "note.txt"
    word = input("Enter the word to search: ")
    client_request(filename, word)
