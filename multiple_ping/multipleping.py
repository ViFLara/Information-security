import os
import time

with open('hosts.txt') as file:
    dump = file.read()
    dump = dump.splitlines()

    for ip in dump:
        print('Verifying ip: ', ip)
        print('-' * 60)
        os.system('ping -c 2 {}' .format(ip))
        print('-' * 60)
        time.sleep(5)

