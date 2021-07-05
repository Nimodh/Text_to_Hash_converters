import hashlib

def main():
    text = input("Type a text to convert it to hash_sha3_256\n")
    hash_object = hashlib.sha3_256(text.encode())
    sha3_256_hash = hash_object.hexdigest()
    print(sha3_256_hash)
    e= input()
    return

main()

