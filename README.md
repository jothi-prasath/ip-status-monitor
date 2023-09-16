## IP Status Monitor

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.x-green.svg)

IP Status Monitor is a simple Flask web application that allows you to monitor the status of multiple IP addresses defined in a configuration file. It uses the `ping3` library to determine whether an IP address is alive or dead.

### Getting Started

1. Clone this repository to your local machine.
```bash
git clone https://github.com/jothi-prasath/ip-status-monitor.git
cd IPStatusChecker
```
2. Install the required Python packages.
```bash
pip install -r requirements.txt
```
3. Configure your IP addresses and settings in the `config.txt` file.
```yml
# Sample Configuration File
interval: 5  # ping interval in seconds
192.168.1.1
192.168.1.2
192.168.1.3
```
4. Run the application.
```bash
python app.py
```
5. Access the web application in your browser at http://localhost:5000.