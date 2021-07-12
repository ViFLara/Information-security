import os  # Integrates the programs or resources of the Operating System

print("#" * 60)

ip_or_host = input("Type the IP or host to be checked: ")

print("-" * 60)

os.system('ping -c 6 {}' .format(ip_or_host))  # -c -> Set limit to desire number of ping packets

print("-" * 60)