from subprocess import Popen
import sys


def bazylek_help():
    return "0 Param : python run_bazylek.py\n" \
           "1 Param : python run_bazylek.py <password>\n" \
           "2 Param : python run_bazylek.py <name> <password>\n" \
           "HELP    : python run_bazylek.py --help"

name = "ssid="
key = "key="
status = False

if len(sys.argv) == 1:
    name += input("Set network NAME     : ", )
    key += input("Set network PASSWORD : ")
    status = True
elif len(sys.argv) == 2:
    if sys.argv[1] == '--help' or sys.argv[1] == '-help':
        print(bazylek_help())
    elif len(sys.argv[1]) > 8:
        name = "ssid=Bazylek"
        key += sys.argv[1]
        status = True
elif len(sys.argv) == 3:
    name += sys.argv[1]
    key += sys.argv[2]
    status = True

if status:
    print("Creating hotspot "+name+" !")
    Popen(['netsh', 'wlan', 'set', 'hostednetwork', 'mode=allow', name, key], shell=True)
    Popen(['netsh', 'wlan', 'start', 'hostednetwork'], shell=True)
    print("")
else:
    print ("For help type -help or --help")