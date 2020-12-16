import hashlib; import threading
import os; import time
from termcolor import colored
import colorama

colorama.init()

BANNER1 = colored('''
  ██░ ██  ▄▄▄        ██████  ██░ ██  ███▄    █  ██▓ ███▄    █  ▄▄▄██▀▀▀▄▄▄
 ▓██░ ██▒▒████▄    ▒██    ▒ ▓██░ ██▒ ██ ▀█   █ ▓██▒ ██ ▀█   █    ▒██  ▒████▄
 ▒██▀▀██░▒██  ▀█▄  ░ ▓██▄   ▒██▀▀██░▓██  ▀█ ██▒▒██▒▓██  ▀█ ██▒   ░██  ▒██  ▀█▄
 ░▓█ ░██ ░██▄▄▄▄██   ▒   ██▒░▓█ ░██ ▓██▒  ▐▌██▒░██░▓██▒  ▐▌██▒▓██▄██▓ ░██▄▄▄▄██
 ░▓█▒░██▓ ▓█   ▓██▒▒██████▒▒░▓█▒░██▓▒██░   ▓██░░██░▒██░   ▓██░ ▓███▒   ▓█   ▓██▒
  ▒ ░░▒░▒ ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒░ ▒░   ▒ ▒ ░▓  ░ ▒░   ▒ ▒  ▒▓▒▒░   ▒▒   ▓▒█░
  ▒ ░▒░ ░  ▒   ▒▒ ░░ ░▒  ░ ░ ▒ ░▒░ ░░ ░░   ░ ▒░ ▒ ░░ ░░   ░ ▒░ ▒ ░▒░    ▒   ▒▒ ░
  ░  ░░ ░  ░   ▒   ░  ░  ░   ░  ░░ ░   ░   ░ ░  ▒ ░   ░   ░ ░  ░ ░ ░    ░   ▒
  ░  ░  ░      ░  ░      ░   ░  ░  ░         ░  ░           ░  ░   ░        ░  ░''', 'blue')
BANNER2 = colored('''            ------------------------------------------------------''', 'blue')
BANNER3 = colored('''            || HashNinja: The Dictionary Attack Tool for Hashes ||''', 'red')
BANNER4 = colored('''            ------------------------------------------------------''', 'blue')


def printBanner():
    print(BANNER1), print(BANNER2), print(BANNER3), print(BANNER4)


def generator():
    with open(dictionary, "r") as file:
        for line in file:
            line = line.strip()
            yield line


class AttackFunctions:

    def attackHash1(passwordList, chunkOne):
        for line in passwordList[0:chunkOne]:
            encoded = line.encode("utf-8").strip()
            hashObject = hashify(encoded)
            hash = hashObject.hexdigest()
            if supplied == hash:
                print(colored(f" Found! Dehashed string: {line}", "green"))
                completionTime = time.time() - start
                print(f"Task completed in {completionTime} seconds.")
                print("\nYou may now exit this window.")
                input()

    def attackHash2(passwordList, chunkOne, chunkTwo):
        for line in passwordList[chunkTwo - 1:chunkOne - 1:-1]:
            encoded = line.encode("utf-8").strip()
            hashObject = hashify(encoded)
            hash = hashObject.hexdigest()
            if supplied == hash:
                print(colored(f" Found! Dehashed string: {line}", "green"))
                completionTime = time.time() - start
                print(f"Task completed in {completionTime} seconds.")
                print("\nYou may now exit this window.")
                input()

    def attackHash3(passwordList, chunkTwo, chunkThree):
        for line in passwordList[chunkTwo:chunkThree]:
            encoded = line.encode("utf-8").strip()
            hashObject = hashify(encoded)
            hash = hashObject.hexdigest()
            if supplied == hash:
                print(colored(f" Found! Dehashed string: {line}", "green"))
                completionTime = time.time() - start
                print(f"Task completed in {completionTime} seconds.")
                print("\nYou may now exit this window.")
                input()

    def attackHash4(passwordList, chunkThree, chunkFour):
        for line in passwordList[chunkFour - 1:chunkThree - 1:-1]:
            encoded = line.encode("utf-8").strip()
            hashObject = hashify(encoded)
            hash = hashObject.hexdigest()
            if supplied == hash:
                print(colored(f" Found! Dehashed string: {line}", "green"))
                completionTime = time.time() - start
                print(f"Task completed in {completionTime} seconds.")
                print("\nYou may now exit this window.")
                input()

    def attackHash5(passwordList, chunkFour, chunkFive):
        for line in passwordList[chunkFour:chunkFive]:
            encoded = line.encode("utf-8").strip()
            hashObject = hashify(encoded)
            hash = hashObject.hexdigest()
            if supplied == hash:
                print(colored(f" Found! Dehashed string: {line}", "green"))
                completionTime = time.time() - start
                print(f"Task completed in {completionTime} seconds.")
                print("\nYou may now exit this window.")
                input()

    def attackHash6(passwordList, chunkFive, chunkSix):
        for line in passwordList[chunkSix - 1:chunkFive - 1:-1]:
            encoded = line.encode("utf-8").strip()
            hashObject = hashify(encoded)
            hash = hashObject.hexdigest()
            if supplied == hash:
                print(colored(f" Found! Dehashed string: {line}", "green"))
                completionTime = time.time() - start
                print(f"Task completed in {completionTime} seconds.")
                print("\nYou may now exit this window.")
                input()

    def attackHash7(passwordList, chunkSix, chunkSeven):
        for line in passwordList[chunkSix:chunkSeven]:
            encoded = line.encode("utf-8").strip()
            hashObject = hashify(encoded)
            hash = hashObject.hexdigest()
            if supplied == hash:
                print(colored(f" Found! Dehashed string: {line}", "green"))
                completionTime = time.time() - start
                print(f"Task completed in {completionTime} seconds.")
                print("\nYou may now exit this window.")
                input()

    def attackHash8(passwordList, chunkSeven):
        for line in passwordList[:chunkSeven - 1:-1]:
            encoded = line.encode("utf-8").strip()
            hashObject = hashify(encoded)
            hash = hashObject.hexdigest()
            if supplied == hash:
                print(colored(f" Found! Dehashed string: {line}", "green"))
                completionTime = time.time() - start
                print(f"Task completed in {completionTime} seconds.")
                print("\nYou may now exit this window.")
                input()


def clrscr():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')
    printBanner()


if __name__ == '__main__':

    printBanner()

    try:

        while(True):
            print("\nAlgorithms:-\n")
            hashNames = ["BLAKE2b", "BLAKE2s", "MD5", "SHA-1", "SHA-2 (224-bit)", "SHA-2 (256-bit)",
                         "SHA-2 (384-bit)", "SHA-2 (512-bit)", "SHA-3 (224-bit)", "SHA-3 (256-bit)",
                         "SHA-3 (384-bit)", "SHA-3 (512-bit)", "SHAKE-128", "SHAKE-256"]
            for index, hashName in enumerate(hashNames, start=1):
                print(f"{index:>2}. {hashName}")

            algorithm = input("\n\nSelect algorithm number: ") or "0"

            if algorithm:
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
            supplied = input(f"\nEnter {hashNames[(int(algorithm) - 1)]} hash to attack: ")
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
        print("\nPreparing...", end="")
        generatedList = generator()
        passwordList = list(generatedList)
        print(colored(" Done!", "green"))

        chunkOne = len(passwordList) // 8
        chunkTwo = chunkOne * 2
        chunkThree = chunkOne * 3
        chunkFour = chunkOne * 4
        chunkFive = chunkOne * 5
        chunkSix = chunkOne * 6
        chunkSeven = chunkOne * 7

        threadForwardOne = threading.Thread(target=AttackFunctions.attackHash1, args=[passwordList, chunkOne])
        threadReverseOne = threading.Thread(target=AttackFunctions.attackHash2, args=[passwordList, chunkOne, chunkTwo])

        threadForwardTwo = threading.Thread(target=AttackFunctions.attackHash3, args=[passwordList, chunkTwo, chunkThree])
        threadReverseTwo = threading.Thread(target=AttackFunctions.attackHash4, args=[passwordList, chunkThree, chunkFour])

        threadForwardThree = threading.Thread(target=AttackFunctions.attackHash5, args=[passwordList, chunkFour, chunkFive])
        threadReverseThree = threading.Thread(target=AttackFunctions.attackHash6, args=[passwordList, chunkFive, chunkSix])

        threadForwardFour = threading.Thread(target=AttackFunctions.attackHash7, args=[passwordList, chunkSix, chunkSeven])
        threadReverseFour = threading.Thread(target=AttackFunctions.attackHash8, args=[passwordList, chunkSeven])

        clrscr()
        print("\nWorking...", end="")

        start = time.time()

        threadPool = [threadForwardOne, threadReverseOne, threadForwardTwo, threadReverseTwo,
                      threadForwardThree, threadReverseThree, threadForwardFour, threadReverseFour]

        for thread in threadPool:
            thread.start()

        for thread in threadPool:
            thread.join()
    except KeyboardInterrupt:
        clrscr()
        print("\nCTRL ^C\n\nThrew a wrench in the works.")
        print("Press Enter to exit.")
        input()
