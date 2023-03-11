try:
    from colorama import Back, Fore, Style
    import glob, os
    import random
    import string
    import time
    import fade
    import os

except:
    import time
        
    print("[-] Error! You Dont Have All The Required Modules Installed To Run Batch Obfuscater V2.1 Open install.bat To Fix!")
    time.sleep(5)
    exit()



text = """
 ▒█████   ▄▄▄▄     █████▒█    ██   ██████  ▄████▄   ▄▄▄     ▄▄▄█████▓ ▒█████   ██▀███  
▒██▒  ██▒▓█████▄ ▓██   ▒ ██  ▓██▒▒██    ▒ ▒██▀ ▀█  ▒████▄   ▓  ██▒ ▓▒▒██▒  ██▒▓██ ▒ ██▒
▒██░  ██▒▒██▒ ▄██▒████ ░▓██  ▒██░░ ▓██▄   ▒▓█    ▄ ▒██  ▀█▄ ▒ ▓██░ ▒░▒██░  ██▒▓██ ░▄█ ▒
▒██   ██░▒██░█▀  ░▓█▒  ░▓▓█  ░██░  ▒   ██▒▒▓▓▄ ▄██▒░██▄▄▄▄██░ ▓██▓ ░ ▒██   ██░▒██▀▀█▄  
░ ████▓▒░░▓█  ▀█▓░▒█░   ▒▒█████▓ ▒██████▒▒▒ ▓███▀ ░ ▓█   ▓██▒ ▒██▒ ░ ░ ████▓▒░░██▓ ▒██▒
░ ▒░▒░▒░ ░▒▓███▀▒ ▒ ░   ░▒▓▒ ▒ ▒ ▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░ ▒▒   ▓▒█░ ▒ ░░   ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░
  ░ ▒ ▒░ ▒░▒   ░  ░     ░░▒░ ░ ░ ░ ░▒  ░ ░  ░  ▒     ▒   ▒▒ ░   ░      ░ ▒ ▒░   ░▒ ░ ▒░
░ ░ ░ ▒   ░    ░  ░ ░    ░░░ ░ ░ ░  ░  ░  ░          ░   ▒    ░      ░ ░ ░ ▒    ░░   ░ 
    ░ ░   ░                ░           ░  ░ ░            ░  ░            ░ ░     ░     
               ░                          ░                                            

Batch Obfuscater | V2.1
DevBubba#6642    

"""

banner = fade.fire(text)

def main() -> None:
  print(banner)
  auto_detect = input('{:<27}: '.format(f"{Fore.YELLOW}[+] AutoDetect .Bat File [Y/N]  {Style.RESET_ALL}"))
  path = ''
  if auto_detect == "Y":
    os.getcwd()
    for file in glob.glob("*.bat"):
      print(f"{Fore.GREEN}[+] AutoDetected .Bat File - {file}{Style.RESET_ALL}")
      path = file

  elif auto_detect == "y":
    os.getcwd()
    for file in glob.glob("*.bat"):
      print(f"{Fore.GREEN}[+] AutoDetected .Bat File - {file}{Style.RESET_ALL}")
      path = file
      
  elif auto_detect == "N":
    path = input('{:<27}: '.format(f"{Fore.YELLOW}[+] File Path Including (.bat)  {Style.RESET_ALL}"))
    os.getcwd()
    for file in glob.glob(path):
      print(f"{Fore.GREEN}[+] Found .Bat File - {file}{Style.RESET_ALL}")

  elif auto_detect == "n":
    path = input('{:<27}: '.format(f'{Fore.YELLOW}[+] File Path Including (.bat)  {Style.RESET_ALL}'))
    os.getcwd()
    for file in glob.glob(path):
      print(f"{Fore.GREEN}[+] Found .Bat File - {file}{Style.RESET_ALL}")

  else:
    print(f"{Fore.RED}[-] Please Enter A Valid Argument!{Style.RESET_ALL}")
    print(f"{Fore.RED}[-] Exiting...{Style.RESET_ALL}")
    time.sleep(5)
    exit()

  level = int(input('{:<27}: '.format(f'{Fore.YELLOW}[+] Obfuscation Level [1/2]  {Style.RESET_ALL}')))

  confirm = input('{:<27}: '.format(f"{Fore.YELLOW}[+] Are You Sure You Would Like To Obfuscate {file}? [Y/N]  {Style.RESET_ALL}"))

  with open(path, 'r', encoding='utf-8') as f:
    code = f.read()

  if confirm == "Y":
    if level == 1:
      with open('obfuscated.bat', 'w') as f:
        f.write(methods.methodOne(code))

    elif level == 2:
      with open('obfuscated.bat', 'wb') as f:
        f.write(methods.methodTwo(code))
    
    print(f"{Fore.GREEN}[+] Succsesfully Obfuscated {file}!{Style.RESET_ALL}")
    print(f"{Fore.RED}[-] Exiting...{Style.RESET_ALL}")
    time.sleep(5)
    exit()

  if confirm == "y":
    with open('obfuscated.bat', 'w') as f:
      f.write(methods.obfuscate(code))
    print(f"{Fore.GREEN}[+] Succsesfully Obfuscated {file}!{Style.RESET_ALL}")
    print(f"{Fore.RED}[-] Exiting...{Style.RESET_ALL}")
    time.sleep(5)
    exit()

  if confirm == "N":
    print(f"{Fore.RED}[-] Cancelled Obfuscation!{Style.RESET_ALL}")
    print(f"{Fore.RED}[-] Exiting...{Style.RESET_ALL}")
    time.sleep(5)
    exit()

  if confirm == "n":
    print(f"{Fore.RED}[-] Cancelled Obfuscation!{Style.RESET_ALL}")
    print(f"{Fore.RED}[-] Exiting...{Style.RESET_ALL}")
    time.sleep(5)
    exit()
    
  else:
    print(f"{Fore.RED}[-] Please Enter A Valid Argument!{Style.RESET_ALL}")
    print(f"{Fore.RED}[-] Exiting...{Style.RESET_ALL}")
    time.sleep(5)
    exit()

class methods:

  def methodOne(code: str) -> str:
    obfuscated = ''
    for lines in code:
      for char in lines:
        if char == '\n':
          obfuscated += char

        elif char == '%':
          obfuscated += char
          while char != '%':
            char = next(lines)
            obfuscated += char

        else:
          ran_str = ''.join(
            random.choice(string.ascii_letters)
            for _ in range(random.randint(5, 15)))
          obfuscated += f'{char}%{ran_str}%'
    return obfuscated

  def methodTwo(code: str) -> str:
    code = bytes(methods.methodOne(code), 'utf-8')

    obfuscated = []
    obfuscated.extend(['FF', 'FE', '0A', '0D'])
    obfuscated.extend(['{:02X}'.format(b) for b in code])
    obfuscated = bytes.fromhex(''.join(obfuscated))

    return obfuscated

if __name__ == '__main__':
  main()