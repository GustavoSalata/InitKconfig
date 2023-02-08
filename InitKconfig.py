#!/usr/bin/python

import os

#update na máquina 
os.system("apt update -y")

#Ferramentas internas essenciais
os.system("apt install hydra -y")
os.system("apt install nmap -y")
os.system("apt install subfinder -y")
os.system("apt install dnsx -y")
os.system("apt install dirb -y")
os.system("apt install gobuster -y")

#Ferramentas externas essenciais
os.system("wget https://raw.githubusercontent.com/julimar155/headergap/main/headergapv4.1.py")



#Worlists
os.system("apt install seclists -y")
