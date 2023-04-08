import sys
import os
import time
import string
import random
import subprocess

from colorama import Back, Fore, Style
import fade
import glob

if sys.version_info < (3, 0):
    raise Exception("BatchShield Requires Python Version 3.0 Or Greater")
elif sys.version_info < (3, 10):
    print("Warning! BatchSheild Has Only Been Tested With Python 3.10, But May Work With Other Python 3 Versions!")

required_modules = ["colorama", "fade", "glob"]
missing_modules = []

for module in required_modules:
    try:
        __import__(module)
      
    except ImportError:
        missing_modules.append(module)

if missing_modules:
    print("[-] Error! You Don't Have All The Required Modules Installed To Run BatchShield V2.2!")
  
    if input("Would You Like To Automatically Install Any Missing Modules? [y/n] :  ").lower() == "y":
      
        for module in missing_modules:
            subprocess.call(['pip', 'install', module])
        print("All Missing Modules Have Been Installed, Please Re-Run BatchShield!")
        time.sleep(5)
        exit()
      
    else:
        error_message = "Error Missing Module - '{module}' "
      
        for module in missing_modules:
            print(f"[-] {error_message.format(module=module)}")
          
        time.sleep(5)
        exit()

text = """
\n\n\n
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

BatchShield | V2.3
DevBubba#6642 + goofy#6999
Discord : https://discord.com/6qAvAephsW
"""

print(fade.fire(text))
def main():
    auto_detect = input('{:<27}: '.format(f"{Fore.YELLOW}[+] AutoDetect .Bat File [Y/N]  {Style.RESET_ALL}"))
    path = ''

    if auto_detect.lower() == "y":
        os.getcwd()
        bat_files = glob.glob("*.bat")
        if not bat_files:
            print(f"{Fore.RED}[-] No .Bat Files Found!{Style.RESET_ALL}")
            print(f"{Fore.RED}[-] Exiting...{Style.RESET_ALL}")
            time.sleep(5)
            exit()
        elif len(bat_files) > 1:
            print(f"{Fore.GREEN}[+] Multiple .Bat Files Found!{Style.RESET_ALL}")
            for idx, file in enumerate(bat_files):
                print(f"{Fore.RED}[{idx+1}] {file}{Style.RESET_ALL}")
            try:
                selection = int(input('{:<27}: '.format(f"{Fore.YELLOW}[+] Select File [1-{len(bat_files)}]  {Style.RESET_ALL}")))
                if selection < 1 or selection > len(bat_files):
                    raise ValueError
            except ValueError:
                print(f"{Fore.RED}[-] Invalid Input!{Style.RESET_ALL}")
                print(f"{Fore.RED}[-] Exiting...{Style.RESET_ALL}")
                time.sleep(5)
                exit()
            path = bat_files[selection-1]

        else:
            path = bat_files[0]
        print(f"{Fore.GREEN}[+] AutoDetected .Bat File - {path}{Style.RESET_ALL}")
        
    elif auto_detect.lower() == "n":
        path = input('{:<27}: '.format(f"{Fore.YELLOW}[+] File Path Including (.bat)  {Style.RESET_ALL}"))
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
        print(f"{Fore.RED}[-] Invalid Input!{Style.RESET_ALL}")
        print(f"{Fore.RED}[-] Exiting...{Style.RESET_ALL}")
        time.sleep(5)
        exit()

    try:
        level = int(input('{:<27}: '.format(f'{Fore.YELLOW}[+] Obfuscation Level [1/2]  {Style.RESET_ALL}')))
        if level not in [1, 2]:
            raise ValueError
    except ValueError:
        print(f"{Fore.RED}[-] Invalid Input!{Style.RESET_ALL}")
        print(f"{Fore.RED}[-] Exiting...{Style.RESET_ALL}")
        time.sleep(5)
        exit()

    confirm = input('{:<27}: '.format(f"{Fore.YELLOW}[+] Are You Sure You Would Like To Obfuscate {path}? [Y/N]  {Style.RESET_ALL}"))

    with open(path, 'r', encoding='utf-8') as f:
        code = f.read()

    if confirm.lower() == "y":
        try:
            if level == 1:
                with open(f'obfuscated_{os.path.basename(path)}', 'w+', encoding='utf-8') as f:
                    try:
                        f.write(Methods.LevelOne(code))
                    except Exception as e:
                        print(f"{Fore.RED}[-] Error: {e}{Style.RESET_ALL}")
                        print(f"{Fore.RED}[-] Exiting...{Style.RESET_ALL}")
                        time.sleep(5)
                        exit()
            elif level == 2:
                with open(f'obfuscated_{os.path.basename(path)}', 'w+', encoding='utf-8') as f:
                    try:
                        f.write(Methods.LevelTwo(code))
                    except Exception as e:
                        print(f"{Fore.RED}[-] Error: {e}{Style.RESET_ALL}")
                        print(f"{Fore.RED}[-] Exiting...{Style.RESET_ALL}")
                        time.sleep(5)
                        exit()
                
            print(f"{Fore.GREEN}[+] Successfully Obfuscated {path}!{Style.RESET_ALL}")
            print(f"{Fore.RED}[-] Exiting...{Style.RESET_ALL}")
            time.sleep(5)
            exit()
        except Exception as e:
            print(f"{Fore.RED}[-] Error: {e}{Style.RESET_ALL}")
            print(f"{Fore.RED}[-] Exiting...{Style.RESET_ALL}")
            time.sleep(5)
            exit()


class Methods:
    @staticmethod
    def LevelOne(code: str) -> str:
        if not isinstance(code, str):
            raise TypeError("Input 'code' Parameter Must Be A String Type!")
        if not code.strip():
            raise ValueError("Input 'code' Parameter Cannot Be Empty!")

        obfuscated = ''
        for line in code.splitlines():
            for char in line:
                if char == '%':
                    ran_str = ''.join(
                        random.choice(string.ascii_letters)
                        for _ in range(random.randint(5, 15)))
                    obfuscated += f'%{ran_str}%'
                else:
                    obfuscated += char
        if not obfuscated.strip():
            raise ValueError("Output From 'LevelOne()' Method Cannot Be Empty!")
        return obfuscated

    @staticmethod
    def LevelTwo(code: str, path: str) -> bytes:
        if not isinstance(code, str):
            raise TypeError("Input 'code' Parameter Must Be A String Type!")
        if not code.strip():
            raise ValueError("Input 'code' Parameter Cannot Be Empty!")

        obfuscated = bytearray(b'\xFF\xFE\n\r')
        encoded = Methods.LevelOne(code)
        try:
            code_bytes = encoded.encode('utf-8', 'strict')
        except UnicodeEncodeError:
            raise ValueError("Cannot Encode Obfuscated Code In UTF-8!")
        if not code_bytes:
            raise ValueError("Output From 'encode()' Method In 'LevelTwo()' Method Cannot Be Empty!")

        if not all(c in string.printable for c in encoded):
            raise ValueError("Input 'code' Parameter Contains Non-Printable Characters!")

        if not all(ord(c) < 128 for c in encoded):
            raise ValueError("Input 'code' Parameter Contains Characters Not Supported By The UTF-8 Encoding!")

        with open(f'obfuscated_{os.path.basename(path)}', 'wb') as f:
            f.write(obfuscated + code_bytes)

        if not obfuscated:
            raise ValueError("Output From 'LevelTwo()' Method Cannot Be Empty!")
        return bytes(obfuscated)

if __name__ == '__main__':
  main()
