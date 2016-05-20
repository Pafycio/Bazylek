from subprocess import Popen
Popen(['netsh', 'wlan', 'stop', 'hostednetwork'], shell=True)