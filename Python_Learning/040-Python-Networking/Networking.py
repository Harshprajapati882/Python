# Python Networking Examples

# 1. Socket Programming: A simple TCP Server and Client

# TCP Server
import socket

def run_server():
    """
    This function runs a simple TCP server.
    """
    # Create a socket object
    # AF_INET: Address Family -> IPv4
    # SOCK_STREAM: Socket Type -> TCP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Get local machine name
    host = socket.gethostname()
    port = 12345

    # Bind to the port
    server_socket.bind((host, port))

    # Queue up to 5 requests
    server_socket.listen(5)

    print(f"Server listening on {host}:{port}")

    while True:
        # Establish a connection
        client_socket, addr = server_socket.accept()
        print(f"Got a connection from {addr}")

        # Send a thank you message to the client.
        message = 'Thank you for connecting'
        client_socket.send(message.encode('ascii'))
        client_socket.close()

# TCP Client
def run_client():
    """
    This function runs a simple TCP client.
    """
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Get local machine name
    host = socket.gethostname()
    port = 12345

    # Connection to hostname on the port.
    client_socket.connect((host, port))

    # Receive no more than 1024 bytes
    message = client_socket.recv(1024)
    client_socket.close()

    print(f"Received from server: {message.decode('ascii')}")

# To run this example:
# 1. Open two terminals.
# 2. In the first terminal, run this script and call run_server().
# 3. In the second terminal, run this script and call run_client().
# Example:
# if __name__ == '__main__':
#     # To run the server
#     run_server()
#
#     # To run the client (in a separate terminal)
#     # run_client()


# 2. URL Processing with urllib

import urllib.request
import urllib.parse

def fetch_url_data():
    """
    Demonstrates how to fetch data from a URL.
    """
    try:
        with urllib.request.urlopen('https://www.python.org') as response:
            html = response.read()
            print("Successfully fetched the content of python.org")
            print("First 100 characters:", html[:100])
    except Exception as e:
        print(f"An error occurred: {e}")

def submit_data_to_form():
    """
    Demonstrates how to submit data to a web form (POST request).
    """
    url = 'https://www.httpbin.org/post'
    params = {
        'name': 'John Doe',
        'email': 'john.doe@example.com'
    }

    # Encode the parameters
    query_string = urllib.parse.urlencode(params)
    data = query_string.encode('ascii')

    try:
        with urllib.request.urlopen(url, data) as response:
            response_data = response.read()
            print("\nResponse from httpbin.org/post:")
            print(response_data.decode('utf-8'))
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == '__main__':
    print("--- URL Processing Examples ---")
    fetch_url_data()
    submit_data_to_form()

    print("\n--- Socket Programming ---")
    print("To test the socket server/client, you need to run them in separate terminals.")
    print("Example: python Networking.py (and uncomment the function calls)")
    # To test server and client:
    # 1. Uncomment run_server() and run the script.
    # 2. Open another terminal, uncomment run_client() and run the script again.
    # import sys
    # if len(sys.argv) > 1 and sys.argv[1] == 'server':
    #     run_server()
    # elif len(sys.argv) > 1 and sys.argv[1] == 'client':
    #     run_client()

