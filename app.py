from flask import Flask, render_template
from ping3 import ping

app = Flask(__name__)

CONFIG_FILE = 'config.txt'

def get_ip_status(ip):
    response_time = ping(ip, timeout=0.1) # timeout 0.1 seconds for local devices
    if response_time is not None:
        return "alive"
    else:
        return "dead"

def read_ip_config():
    ips = []
    interval = 5    #default interval
    with open(CONFIG_FILE, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith("interval:"):
                try:
                    interval = int(line.split(":")[1])
                except:
                    pass
            elif line.startswith("#"):
                pass
            else:
                ips.append(line)
    return ips, interval

@app.route('/')
def index():
    ips, interval = read_ip_config()
    ip_status = {}

    for ip in ips:
        status = get_ip_status(ip)
        ip_status[ip] = status

    return render_template('index.html', ip_status=ip_status, interval=interval)

if __name__ == '__main__':
    app.run(host='localhost',debug=True)
