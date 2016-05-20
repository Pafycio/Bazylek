from subprocess import Popen
from sys import argv


def bazylek_help():
    return "        <  <  <  Bazylek WiFi >  >  >   \n" \
           "                 ||  USAGE ||  \n" \
           " | python run_bazylek.py                    >\n" \
           " | python run_bazylek.py <password>         >\n" \
           " | python run_bazylek.py <name> <password>  >\n"

name = ""
key = ""
status = False

if len(argv) == 1:
    name += input("Set network NAME     : ")
    key += input("Set network PASSWORD : ")
    status = True
elif len(argv) == 2:
    if argv[1] == '--help' or argv[1] == '-help':
        print(bazylek_help())
    else:
        name += "Bazylek"
        key += argv[1]
        status = True
elif len(argv) == 3:
    name += argv[1]
    key += argv[2]
    status = True

if status and len(key) > 7:
    print("Creating hotspot "+name+" < <|> >")
    Popen(['netsh', 'wlan', 'set', 'hostednetwork', 'mode=allow', "ssid="+name, "key="+key], shell=True)
    Popen(['netsh', 'wlan', 'start', 'hostednetwork'], shell=True)
else:
    print("Password must be at least 8 chars long !\n"
          "For help type -help or --help\n")