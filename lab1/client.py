import socket

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket.connect(('localhost', 5000))
print("Соединение установлено")

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

msg_order = 0
while True:
    msg = input("Введите сообщение для отправки: ")
    msg_with_order = str(msg_order) + "|" + msg
    udp_socket.sendto(msg_with_order.encode(), ('localhost', 5001))

    ack_data, address = udp_socket.recvfrom(1024)
    ack = ack_data.decode()

    if int(ack) == msg_order:
        print("Подтвержденное сообщение:", msg)
        msg_order += 1
    else:
        print("Неправильный порядок сообщение:", msg)
