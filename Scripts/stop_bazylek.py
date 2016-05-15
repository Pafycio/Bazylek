import subprocess
subprocess.Popen(['netsh', 'wlan', 'stop', 'hostednetwork'], shell=True)