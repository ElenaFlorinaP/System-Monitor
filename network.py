import socket

def check_internet():
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=3)
        return "ONLINE "
    except OSError:
        return "OFFLINE"
