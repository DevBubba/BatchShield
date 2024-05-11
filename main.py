import sys
import os
import time
import string
import random
import subprocess


banner = """
 ▄▄▄▄    ▄▄▄     ▄▄▄█████▓ ▄████▄   ██░ ██   ██████  ██░ ██  ██▓▓█████  ██▓    ▓█████▄ 
▓█████▄ ▒████▄   ▓  ██▒ ▓▒▒██▀ ▀█  ▓██░ ██▒▒██    ▒ ▓██░ ██▒▓██▒▓█   ▀ ▓██▒    ▒██▀ ██▌
▒██▒ ▄██▒██  ▀█▄ ▒ ▓██░ ▒░▒▓█    ▄ ▒██▀▀██░░ ▓██▄   ▒██▀▀██░▒██▒▒███   ▒██░    ░██   █▌
▒██░█▀  ░██▄▄▄▄██░ ▓██▓ ░ ▒▓▓▄ ▄██▒░▓█ ░██   ▒   ██▒░▓█ ░██ ░██░▒▓█  ▄ ▒██░    ░▓█▄   ▌
░▓█  ▀█▓ ▓█   ▓██▒ ▒██▒ ░ ▒ ▓███▀ ░░▓█▒░██▓▒██████▒▒░▓█▒░██▓░██░░▒████▒░██████▒░▒████▓ 
░▒▓███▀▒ ▒▒   ▓▒█░ ▒ ░░   ░ ░▒ ▒  ░ ▒ ░░▒░▒▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒░▓  ░░ ▒░ ░░ ▒░▓  ░ ▒▒▓  ▒ 
▒░▒   ░   ▒   ▒▒ ░   ░      ░  ▒    ▒ ░▒░ ░░ ░▒  ░ ░ ▒ ░▒░ ░ ▒ ░ ░ ░  ░░ ░ ▒  ░ ░ ▒  ▒ 
 ░    ░   ░   ▒    ░      ░         ░  ░░ ░░  ░  ░   ░  ░░ ░ ▒ ░   ░     ░ ░    ░ ░  ░ 
 ░            ░  ░        ░ ░       ░  ░  ░      ░   ░  ░  ░ ░     ░  ░    ░  ░   ░    
      ░                   ░                                                     ░                                 

Discord     | https://discord.com/6qAvAephsW
Made By     | DevBubba
Version     | V2.2
"""

header = """ :: ▄▄▄▄    ▄▄▄     ▄▄▄█████▓ ▄████▄   ██░ ██   ██████  ██░ ██  ██▓▓█████  ██▓    ▓█████▄ 
:: ▓█████▄ ▒████▄   ▓  ██▒ ▓▒▒██▀ ▀█  ▓██░ ██▒▒██    ▒ ▓██░ ██▒▓██▒▓█   ▀ ▓██▒    ▒██▀ ██▌
:: ▒██▒ ▄██▒██  ▀█▄ ▒ ▓██░ ▒░▒▓█    ▄ ▒██▀▀██░░ ▓██▄   ▒██▀▀██░▒██▒▒███   ▒██░    ░██   █▌
:: ▒██░█▀  ░██▄▄▄▄██░ ▓██▓ ░ ▒▓▓▄ ▄██▒░▓█ ░██   ▒   ██▒░▓█ ░██ ░██░▒▓█  ▄ ▒██░    ░▓█▄   ▌
:: ░▓█  ▀█▓ ▓█   ▓██▒ ▒██▒ ░ ▒ ▓███▀ ░░▓█▒░██▓▒██████▒▒░▓█▒░██▓░██░░▒████▒░██████▒░▒████▓ 
:: ░▒▓███▀▒ ▒▒   ▓▒█░ ▒ ░░   ░ ░▒ ▒  ░ ▒ ░░▒░▒▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒░▓  ░░ ▒░ ░░ ▒░▓  ░ ▒▒▓  ▒ 
:: ▒░▒   ░   ▒   ▒▒ ░   ░      ░  ▒    ▒ ░▒░ ░░ ░▒  ░ ░ ▒ ░▒░ ░ ▒ ░ ░ ░  ░░ ░ ▒  ░ ░ ▒  ▒ 
::  ░    ░   ░   ▒    ░      ░         ░  ░░ ░░  ░  ░   ░  ░░ ░ ▒ ░   ░     ░ ░    ░ ░  ░ 
::  ░            ░  ░        ░ ░       ░  ░  ░      ░   ░  ░  ░ ░     ░  ░    ░  ░   ░    
::       ░                   ░                                                     ░            
::
::                          !! Obfuscated By Batchsield !!\n\n
"""


def clear():
    os.system('cls')

def main():
    from colorama import Back, Fore, Style
    import fade
    import glob
    
    clear()
    print(fade.fire(banner))
    
    auto_detect = input('{:<27}: '.format(
        f"{Fore.YELLOW}[+] AutoDetect .Bat Files [Y/N] {Style.RESET_ALL}"))
    path = ''

    if auto_detect.lower() == "y":
        os.getcwd()
        bat_files = glob.glob("*.bat")
        bat_files = [file for file in bat_files if file != "installer.bat"]
        if not bat_files:
            print(f"{Fore.RED}[-] No .Bat Files Found! {Style.RESET_ALL}")
            print(f"{Fore.RED}[-] Exiting... {Style.RESET_ALL}")
            time.sleep(5)
            exit()
        elif len(bat_files) > 1:
            print(
                f"{Fore.GREEN}[+] Multiple .Bat Files Found! {Style.RESET_ALL}")
            for idx, file in enumerate(bat_files):
                print(f"{Fore.RED}[{idx+1}] {file}{Style.RESET_ALL}")
            try:
                selection = int(
                    input('{:<27}: '.format(
                        f"{Fore.YELLOW}[+] Select File [1-{len(bat_files)}] {Style.RESET_ALL}"
                    )))
                if selection < 1 or selection > len(bat_files):
                    raise ValueError
            except ValueError:
                print(f"{Fore.RED}[-] Invalid Input! {Style.RESET_ALL}")
                print(f"{Fore.RED}[-] Exiting... {Style.RESET_ALL}")
                time.sleep(5)
                exit()
            path = bat_files[selection - 1]

        else:
            path = bat_files[0]
        print(
            f"{Fore.GREEN}[+] Selected File - {path}{Style.RESET_ALL}"
        )

    elif auto_detect.lower() == "n":
        path = input('{:<27}: '.format(
            f"{Fore.YELLOW}[+] File Path Including (.bat) {Style.RESET_ALL}"))
        os.getcwd()
        bat_files = glob.glob(path)
        if not bat_files:
            print(f"{Fore.RED}[-] File Not Found!{Style.RESET_ALL}")
            print(f"{Fore.RED}[-] Exiting...{Style.RESET_ALL}")
            time.sleep(5)
            exit()
        path = bat_files[0]
        print(f"{Fore.GREEN}[+] Found .Bat File - {path}{Style.RESET_ALL}")

    else:
        print(f"{Fore.RED}[-] Invalid Input! {Style.RESET_ALL}")
        print(f"{Fore.RED}[-] Exiting... {Style.RESET_ALL}")
        time.sleep(5)
        exit()

    confirm = input('{:<27}: '.format(
        f"{Fore.YELLOW}[+] Are You Sure You Would Like To Obfuscate {path}? [Y/N] {Style.RESET_ALL}"
    ))

    if confirm.lower() == "y":
        try:
            counter = 0
            counter2 = 0

            originalFileName = path
            customFileName = input('{:<27}: '.format(
                f"{Fore.YELLOW}[+] Use Custom Output Filename [Y/N] {Style.RESET_ALL}"
            ))

            if customFileName.lower() == "y":
                outputFileName = input('{:<27}: '.format(
                    f"{Fore.YELLOW}[+] Enter Custom OutPut Filename {Style.RESET_ALL}"
                ))
            elif customFileName.lower() == "n":
                outputFileName = f"{originalFileName.split('.')[0]}_obfuscated"
            else:
                print(f"{Fore.RED}[-] Invalid Input! {Style.RESET_ALL}")
                print(f"{Fore.RED}[-] Exiting... {Style.RESET_ALL}")
                time.sleep(5)
                exit()

            with open(path, 'r', encoding='utf-8') as fileobj:
                try:
                    path, lel = file.split('.')
                except:
                    pass
                f = open(f"{outputFileName}.bat", "a")
                f.truncate(0)
                f.write(header)
                f.close()
                for line in fileobj:
                    if ":" in line:
                        f = open(f"{outputFileName}.bat", "a")
                        f.write(line.rstrip() + '\n')
                        f.close()
                        pass
                    for ch in line:
                        if not counter == 1:
                            if "\n" in ch:
                                f = open(f"{outputFileName}.bat",
                                         "a",
                                         encoding='utf-8')
                                f.write(f"\n")
                                f.close()
                            elif "%" in ch:

                                f = open(f"{outputFileName}.bat",
                                         "a",
                                         encoding='utf-8')
                                f.write(f"%")
                                f.close()
                                counter = 1
                            else:
                                n = random.randint(1, 10)
                                randomi = ''.join(
                                    random.choice(
                                        'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
                                    ) for _ in range(n))
                                f = open(f"{outputFileName}.bat",
                                         "a",
                                         encoding='utf-8')
                                f.write(f"{ch}%{randomi}%")
                                f.close()
                        else:
                            if "%" in ch:
                                f = open(f"{outputFileName}.bat",
                                         "a",
                                         encoding='utf-8')
                                f.write("%")
                                f.close()
                                counter = 0
                            elif "\n" in ch:
                                f = open(f"{outputFileName}.bat",
                                         "a",
                                         encoding='utf-8')
                                f.write(f"\n")
                                f.close()
                            else:
                                f = open(f"{outputFileName}.bat",
                                         "a",
                                         encoding='utf-8')
                                f.write(ch)
                                f.close()

            print(
                f"{Fore.GREEN}[+] Successfully Obfuscated {path}! {Style.RESET_ALL}"
            )
            print(f"{Fore.RED}[-] Exiting... {Style.RESET_ALL}")
            time.sleep(5)
            exit()
        except Exception as e:
            print(f"{Fore.RED}[-] Error: {e} {Style.RESET_ALL}")
            print(f"{Fore.RED}[-] Exiting... {Style.RESET_ALL}")
            time.sleep(5)
            exit()
            
    elif confirm.lower() == "n":
        reselectFile = input('{:<27}: '.format(
            f"{Fore.YELLOW}[+] Reselect Batch File [Y/N] {Style.RESET_ALL}"
        ))

        if reselectFile.lower() == "y":
            main()
        elif reselectFile.lower() == "n":
            print(f"{Fore.RED}[-] Exiting... {Style.RESET_ALL}")
            time.sleep(5)
            exit()
        else:
            print(f"{Fore.RED}[-] Invalid Input! {Style.RESET_ALL}")
            print(f"{Fore.RED}[-] Exiting... {Style.RESET_ALL}")
            time.sleep(5)
            exit()
    else:
        print(f"{Fore.RED}[-] Invalid Input! {Style.RESET_ALL}")
        print(f"{Fore.RED}[-] Exiting... {Style.RESET_ALL}")
        time.sleep(5)
        exit()

if __name__ == '__main__':
    main()
