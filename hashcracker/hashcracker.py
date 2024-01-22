import hashlib
import pyfiglet

BANNER = pyfiglet.figlet_format("HashCracker")
print(BANNER)

print("Valid hash algorithms: MD5")
valid_hash_types = ('MD5')
hash_type = ''

while hash_type not in valid_hash_types:
    hash_type = imput(str("Enter a hashing algorithm you want to use: "))
    if hash_type not in valid_hash_types:
        print("Please enter a valid hashing algorithm.")

