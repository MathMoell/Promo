import http.server
import random
import time
from prometheus_client import start_http_server, Counter, Gauge, Histogram, Summary

print("HTTP Server käivitub...")
print("Rakendus: http://localhost:5000")
print("Mõõdikud: http://localhost:5001/metrics")

# Mõõdikud
REQUESTS = Counter('http_requests_total', 'HTTP päringute koguarv')
ACTIVE_USERS = Gauge('active_users', 'Aktiivsete kasutajate arv')
REQUEST_DURATION = Histogram('request_duration_seconds', 'Päringu kestus sekundites')
RESPONSE_TIME = Summary('response_time_seconds', 'Vastuse aja kokkuvõte')

class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        # Counter - ainult kasvab
        REQUESTS.inc()

        # Gauge - võib tõusta ja langeda
        ACTIVE_USERS.set(random.randint(1, 20))

        # Histogram ja Summary - mõõdavad kestust
        with REQUEST_DURATION.time():
            with RESPONSE_TIME.time():
                time.sleep(random.uniform(0.1, 0.5))
                self.send_response(200)
                self.end_headers()
                self.wfile.write(b'Tere!')

    def log_message(self, format, *args):
        pass  # Vähem logi

if __name__ == '__main__':
    start_http_server(5001)
    server = http.server.HTTPServer(('0.0.0.0', 5000), MyHandler)
    server.serve_forever()
