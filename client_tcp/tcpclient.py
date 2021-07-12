import socket
import sys


def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e:
        print("The connection has failed!")
        print("Error: {}" .format(e))
        sys.exit()
    print("Socket successfully created")

    target_host = input("Type the host or Ip to be connected: ")
    target_port = input("Type the port to be connected: ")

    try:
        s.connect((target_host, int(target_port)))
        print("Tcp client successfully created on Host: " + target_host + " and Port: " + target_port)
        s.shutdown(2)
    except socket.error as e:
        print("Unable to connect to the Host: " + target_host + " - Port: " + target_port)
        print("Error: {}" .format(e))
        sys.exit()


if __name__ == '__main__':
    main()
