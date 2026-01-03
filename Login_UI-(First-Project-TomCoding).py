# You have to install colorama first before editing (pip3 install colorama)
from colorama import Fore, init


def information():  # Definition login steps
    username = input(Fore.CYAN + "Username:").strip()
    input(Fore.MAGENTA + "Password:")
    return username


def accept():  # Definition comfirm choice (Demo)
    choice = input("Are you sure? Y/n:").lower().strip()
    return choice


init(autoreset=True)


text1 = "Please note that this just a demo version, bugs and error may contain in software"
width = 120

print(f"{text1:^{width}}\n")    # Make the text at the center


while True:             # Choice repeat (demo)
    print(Fore.YELLOW +
          "Please choose a choice, L: login , R: Register, E: exit")
    # Input a writable command to terminal
    command = input("---YourName---" + ">>>").strip()

    if command.lower() in ["l", "login"]:   # Show Login UI
        username = information()
        print("Login Successful!")
        print("----------------------------------")
        print(
            f"{Fore.GREEN}Welcome {Fore.WHITE}{username}{Fore.GREEN}!")
        continue

    elif command.lower() in ["e", "exit"]:  # Exit Program
        print(Fore.GREEN + Fore.LIGHTGREEN_EX + "Exiting System.....")
        break

    if not command:
        continue

        # -First project made by TomCoding-
