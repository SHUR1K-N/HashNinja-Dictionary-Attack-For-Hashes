import hashlib
import pyperclip

while (True):
    print("\nAlgorithms:-\n")
    # for index, element in enumerate(sorted(hashlib.algorithms_guaranteed), start=1):
        # print(f"{index:>2}. {element}")
    print('''
1. BLAKE2b
2. BLAKE2s
3. MD5
4. SHA-1
5. SHA-2 (224-bit)
6. SHA-2 (256-bit)
7. SHA-2 (384-bit)
8. SHA-2 (512-bit)
9. SHA-3 (224-bit)
10. SHA-3 (256-bit)
11. SHA-3 (384-bit)
12. SHA-3 (512-bit)
13. SHAKE-128
14. SHAKE-256''')

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
        hashify = getattr(hashlib, "sha512")
    elif algorithm == "9":
        hashify = getattr(hashlib, "sha3_224")
    elif algorithm == "10":
        hashify = getattr(hashlib, "sha3_256")
    elif algorithm == "11":
        hashify = getattr(hashlib, "sha3_384")
    elif algorithm == "12":
        hashify = getattr(hashlib, "sha3_512")
    elif algorithm == "13":
        hashify = getattr(hashlib, "shake_128")
    elif algorithm == "14":
        hashify = getattr(hashlib, "shake_256")
    else:
        print("\nInvalid entry. Choose from the options. Try again.\n")
        continue
    break

decimal = input("Input decimal: ")

hash = decimal.encode("utf-8")
hash = hashify(hash)
hash = hash.hexdigest()
print(f"Hash value: {hash}"), pyperclip.copy(hash)
print("\nHash copied to clipboard.")
print("Press Enter to exit.")
input()
