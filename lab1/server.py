import socket


def main():
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_socket.bind(('localhost', 5000))
    tcp_socket.listen(1)
    print("Ожидание подключения...")

    client_socket, client_address = tcp_socket.accept()
    print("Установлено соединение:", client_address)

    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    udp_socket.bind(("localhost", 5001))

    msg_order = 0

    while True:
        data, address = udp_socket.recvfrom(1024)
        msg = data.decode()
        msg_parts = msg.split("|")

        if int(msg_parts[0]) == msg_order:
            print("Полученное сообщение: ", msg_parts[1])
            msg_order += 1
            print(msg_order)
        else:
            print("Получено сообщение вне очереди:", msg_parts[1])

        ack = str(msg_order - 1).encode()
        udp_socket.sendto(ack, address)


if __name__ == '__main__':
    main()
