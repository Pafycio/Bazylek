import subprocess

key = 'key='+input("Set password for network : ")

subprocess.Popen(['netsh', 'wlan', 'set', 'hostednetwork', 'mode=allow', 'ssid=Bazylek', key], shell=True)
subprocess.Popen(['netsh', 'wlan', 'start', 'hostednetwork'], shell=True)
