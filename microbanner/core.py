import socket

def grab(host, port=80):

    print()
    print("MicroBanner")
    print("=" * 40)

    try:

        sock = socket.create_connection((host, port), timeout=5)

        request = (
            f"HEAD / HTTP/1.0\r\n"
            f"Host: {host}\r\n\r\n"
        )

        sock.send(request.encode())

        data = sock.recv(1024).decode(errors="replace")

        sock.close()

        print(data)

    except Exception as e:

        print("Banner grab failed.")
        print(e)
