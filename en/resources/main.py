import network
import socket
import time
import os

WIFI_TIMEOUT_SECONDS = 20
HOST = "0.0.0.0"
PORT = 80
WEB_ROOT = "www"

try:
    from secrets import WIFI_SSID, WIFI_PASSWORD
except ImportError:
    WIFI_SSID = None
    WIFI_PASSWORD = None


def file_exists(path):
    try:
        stat = os.stat(path)
        return (stat[0] & 0x4000) == 0
    except OSError:
        return False


def send_response(client, status_code, reason, content_type, body):
    headers = [
        "HTTP/1.1 {} {}".format(status_code, reason),
        "Content-Type: {}".format(content_type),
        "Content-Length: {}".format(len(body)),
        "Cache-Control: no-store",
        "Pragma: no-cache",
        "Expires: 0",
        "Connection: close",
        "",
        "",
    ]
    client.send("\r\n".join(headers).encode("utf-8"))
    if body:
        client.send(body)


def send_file(client, file_path):
    try:
        size = os.stat(file_path)[6]
        headers = [
            "HTTP/1.1 200 OK",
            "Content-Type: text/html; charset=utf-8",
            "Content-Length: {}".format(size),
            "Cache-Control: no-store",
            "Pragma: no-cache",
            "Expires: 0",
            "Connection: close",
            "",
            "",
        ]
        client.send("\r\n".join(headers).encode("utf-8"))

        with open(file_path, "rb") as f:
            while True:
                chunk = f.read(1024)
                if not chunk:
                    break
                client.write(chunk)

    except Exception as e:
        body = ("500 Internal Server Error\r\n\r\n{}".format(e)).encode("utf-8")
        send_response(client, 500, "Internal Server Error", "text/plain; charset=utf-8", body)


def connect_wifi():
    if not WIFI_SSID or not WIFI_PASSWORD:
        raise RuntimeError("Missing WIFI_SSID or WIFI_PASSWORD in secrets.py")

    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)

    if wlan.isconnected():
        return wlan

    wlan.connect(WIFI_SSID, WIFI_PASSWORD)

    start = time.time()
    while not wlan.isconnected():
        if time.time() - start > WIFI_TIMEOUT_SECONDS:
            raise RuntimeError("Wi-Fi connection timed out")
        time.sleep(0.25)

    return wlan


def handle_client(client):
    try:
        request = client.recv(1024)
        if not request:
            return

        try:
            request_line = request.decode("utf-8").split("\r\n")[0]
        except UnicodeError:
            send_response(client, 400, "Bad Request", "text/plain; charset=utf-8", b"Bad Request")
            return

        parts = request_line.split()
        if len(parts) < 2:
            send_response(client, 400, "Bad Request", "text/plain; charset=utf-8", b"Bad Request")
            return

        method = parts[0]
        path = parts[1].split("?", 1)[0]

        if method != "GET":
            send_response(client, 405, "Method Not Allowed", "text/plain; charset=utf-8", b"Method Not Allowed")
            return

        if path == "/":
            path = "/index.html"

        file_path = WEB_ROOT + path

        if not file_exists(file_path):
            send_response(client, 404, "Not Found", "text/plain; charset=utf-8", b"404 Not Found")
            return

        send_file(client, file_path)
        time.sleep_ms(100)

    finally:
        try:
            client.close()
        except Exception:
            pass


def serve():
    addr = socket.getaddrinfo(HOST, PORT)[0][-1]
    server = socket.socket()
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(addr)
    server.listen(5)

    while True:
        client, _ = server.accept()
        handle_client(client)


def main():
    wlan = connect_wifi()
    print("Open http://{}/".format(wlan.ifconfig()[0]))
    serve()


main()
