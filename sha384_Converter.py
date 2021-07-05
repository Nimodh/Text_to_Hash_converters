import hashlib

def main():
    text = input("Type a text to convert it to hash_sha384\n")
    hash_object = hashlib.sha384(text.encode())
    sha384_hash = hash_object.hexdigest()
    print(sha384_hash)
    e= input()
    return

main()

