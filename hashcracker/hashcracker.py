import hashlib
import pyfiglet

BANNER = pyfiglet.figlet_format("HashCracker")
print(BANNER)

print("Valid hash algorithms: MD5 | SHA1 | SHA512 | SHA224")
valid_hash_types = ('MD5','SHA1','SHA512','SHA224')
hash_type = ''

while hash_type not in valid_hash_types:
    hash_type = str(input("Choose algorithm: ").upper())
    if hash_type not in valid_hash_types:
        print("Please enter a valid hashing algorithm.")

wordlist_location = input(str("Enter the location of your wordlist: "))
HASH = str(input("Enter your hash: "))

wordlist = open(f"{wordlist_location}").read()
LIST = wordlist.splitlines()

for word in LIST:
    if hash_type == "MD5":
        hash_object = hashlib.md5(f"{word}".encode('utf-8'))
        hashed = hash_object.hexdigest()
        if HASH == hashed:
            print(f"\033[1;32m HASH CRACKED: {word}")

    elif hash_type == "SHA1":
        hash_object = hashlib.sha1(f"{word}".encode('utf-8'))
        hashed = hash_object.hexdigest()
        if HASH == hashed:
            print(f"\033[1;32m HASH CRACKED: {word}")

    elif hash_type == "SHA512":
        hash_object = hashlib.sha512(f"{word}".encode('utf-8'))
        hashed = hash_object.hexdigest()
        if HASH == hashed:
            print(f"\033[1;32m HASH CRACKED: {word}")
    
    elif hash_type == "SHA224":
        hash_object = hashlib.sha224(f"{word}".encode('utf-8'))
        hashed = hash_object.hexdigest()
        if HASH == hashed:
            print(f"\033[1;32m HASH CRACKED: {word}")
