import hashlib; import time; import os
from termcolor import colored
import colorama

colorama.init()

BANNER1 = colored('''
   ██░ ██  ▄▄▄        ██████  ██░ ██  ▄▄▄     ▄▄▄█████▓▄▄▄█████▓ ▄▄▄       ▄████▄   ██ ▄█▀
  ▓██░ ██▒▒████▄    ▒██    ▒ ▓██░ ██▒▒████▄   ▓  ██▒ ▓▒▓  ██▒ ▓▒▒████▄    ▒██▀ ▀█   ██▄█▒
  ▒██▀▀██░▒██  ▀█▄  ░ ▓██▄   ▒██▀▀██░▒██  ▀█▄ ▒ ▓██░ ▒░▒ ▓██░ ▒░▒██  ▀█▄  ▒▓█    ▄ ▓███▄░
  ░▓█ ░██ ░██▄▄▄▄██   ▒   ██▒░▓█ ░██ ░██▄▄▄▄██░ ▓██▓ ░ ░ ▓██▓ ░ ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄
  ░▓█▒░██▓ ▓█   ▓██▒▒██████▒▒░▓█▒░██▓ ▓█   ▓██▒ ▒██▒ ░   ▒██▒ ░  ▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄
   ▒ ░░▒░▒ ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒ ▒▒   ▓▒█░ ▒ ░░     ▒ ░░    ▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒
   ▒ ░▒░ ░  ▒   ▒▒ ░░ ░▒  ░ ░ ▒ ░▒░ ░  ▒   ▒▒ ░   ░        ░      ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░
   ░  ░░ ░  ░   ▒   ░  ░  ░   ░  ░░ ░  ░   ▒    ░        ░        ░   ▒   ░        ░ ░░ ░
   ░  ░  ░      ░  ░      ░   ░  ░  ░      ░  ░                       ░  ░░ ░      ░  ░
                                                                          ░''', 'blue')
BANNER2 = colored('''                  ------------------------------------------------------''', 'blue')
BANNER3 = colored('''                  || HashAttack: The Dictionary Attack Tool for Hashes ||''', 'red')
BANNER4 = colored('''                  ------------------------------------------------------''', 'blue')


def printBanner():
    print(BANNER1), print(BANNER2), print(BANNER3), print(BANNER4)


def attack():
    found = False
    with open(dictionary, "r") as file:
        for tries, line in enumerate(file):
            line = line.encode("utf-8").strip()
            hashObject = hashify(line)
            hash = hashObject.hexdigest()
            if supplied == hash:
                line = str(line)
                print(colored(f" Found! Dehashed string: {line[2:-1]}", "green"))
                found = True
                break
    return(found, tries)


def clrscr():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')
    printBanner()


if __name__ == '__main__':

    printBanner()

    while (True):
        print("\nAlgorithms:-\n")
        for index, element in enumerate(sorted(hashlib.algorithms_guaranteed), start=1):
            print(f"{index:>2}. {element}")

        algorithm = input("\n\nSelect algorithm number: ")

        if algorithm == "1":
            hashify = getattr(hashlib, "blake2b")
        elif algorithm == "2":
            hashify = getattr(hashlib, "blake2s")
        elif algorithm == "3":
            hashify = getattr(hashlib, "md5")
        elif algorithm == "4":
            hashify = getattr(hashlib, "sha1")
        elif algorithm == "5":
            hashify = getattr(hashlib, "sha224")
        elif algorithm == "6":
            hashify = getattr(hashlib, "sha256")
        elif algorithm == "7":
            hashify = getattr(hashlib, "sha384")
        elif algorithm == "8":
            hashify = getattr(hashlib, "sha3_224")
        elif algorithm == "9":
            hashify = getattr(hashlib, "sha3_256")
        elif algorithm == "10":
            hashify = getattr(hashlib, "sha3_384")
        elif algorithm == "11":
            hashify = getattr(hashlib, "sha3_512")
        elif algorithm == "12":
            hashify = getattr(hashlib, "sha512")
        elif algorithm == "13":
            hashify = getattr(hashlib, "shake_128")
        elif algorithm == "14":
            hashify = getattr(hashlib, "shake_256")
        else:
            clrscr()
            print("\nInvalid entry. Choose from the options. Try again.\n")
            continue
        break

    while (True):
        supplied = input("\nInput hash to attack: ")
        if (supplied == "" or len(supplied) < 30):
            clrscr()
            print("\nInvalid entry. Please try again.\n")
            continue
        else:
            break

    while (True):
        dictionary = input("\nEnter dictionary file path here: ")
        if (os.path.isfile(dictionary) is True):
            break
        else:
            clrscr()
            print("\nEither file does not exist or invalid path entered. Try again.\n")
            continue

    clrscr()
    print("\nWorking...", end="")

    start = time.time()
    found, tries = attack()
    completionTime = time.time() - start

    if found:
        try:
            rate = (int(tries) // completionTime)
            print(f"\n\nThe task completed successfully in {completionTime} seconds. (at ~{rate} tries/sec)")
            print("Press any key to exit.")
            input()

        except ZeroDivisionError:
            print("\n\nThe task completed successfully in zero seconds.")
            print("Press any key to exit.")
            input()
    else:
        print(colored(f" Either all lines in {dictionary} tried and exhausted (password not found), or invalid hash supplied.", "red"))
        print(colored("You may try another dictionary file, or verify the hash supplied + hash type.", "red"))
        print("\nPress any key to exit.")
        input()
