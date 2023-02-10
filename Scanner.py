import socket
import threading

def scan(target, port):
    sockets = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sockets.settimeout(5)
    scan = sockets.connect_ex((target, port))
    if scan == 0:
        print(f"Port > {port} open")
    sockets.close()

def ports(target):
    threads = []
    for port in range(1, 65535):
        t = threading.Thread(target=scan, args=(target, port))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

target = input("Enter the target address: ")
ports(target)
