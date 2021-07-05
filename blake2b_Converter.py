import hashlib

def main():
    text = input("Type a text to convert it to hash_blake2b\n")
    hash_object = hashlib.blake2b(text.encode())
    blake2b_hash = hash_object.hexdigest()
    print(blake2b_hash)
    e= input()
    return

main()

