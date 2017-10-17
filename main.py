import socket
from machine import Pin

led_pin = Pin(5, Pin.OUT)
led_pin= Pin(4, Pin.OUT)
led_pin= Pin(0, Pin.OUT)

CONTENT = """\
HTTP/1.0 200 OK
Content-Type: text/html

<html>
  <head>
  </head>
  <body>
    <p>Hello #%d from MicroPython!</p>
    <a href="/toggle">Click here to toggle red LED hooked to pin 5</a>
    <a href="/toggle">Click here to toggle green LED hooked to pin 4</a>
    <a href="/toggle">Click here to toggle blue LED hooked to pin 0</a>
  </body>
</html>
"""

def main():
    s = socket.socket()
    ai = socket.getaddrinfo("10.59.1.166", 8080)
    print("Bind address info:", ai)
    addr = ai[0][-1]

    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(addr)
    s.listen(5)
    print("Listening, connect your browser to http://10.59.1.166:8080/")

    counter = 0
    while True:
        sock, addr = s.accept()
        print("Client address:", addr)
        stream = sock.makefile("rwb")
        req = stream.readline().decode("ascii")
        method, path, protocol = req.split(" ")
        print("Got", method, "request for", path)
        if path == "/toggle":
            led_pin.value(1-led_pin.value())
        while True:
            h = stream.readline().decode("ascii").strip()
            if h == "":
                break
            print("Got HTTP header:", h)
        stream.write((CONTENT % counter).encode("ascii"))
        stream.close()
        sock.close()
        counter += 1
        print()

main()
