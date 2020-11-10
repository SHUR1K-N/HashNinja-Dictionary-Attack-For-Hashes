import hashlib
import pyperclip

print("\nAlgorithms:-\n")
for index, element in enumerate(sorted(hashlib.algorithms_guaranteed), start=1):
    print(f"{index:>2}. {element}")

algorithm = input("\n\nSelect algorithm number: ") or "0"

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

decimal = input("Input decimal: ")

hash = decimal.encode("utf-8")
hash = hashify(hash)
hash = hash.hexdigest()
print(f"Hash value: {hash}"), pyperclip.copy(hash)
print("\nHash copied to clipboard.")
print("Press Enter to exit.")
input()
