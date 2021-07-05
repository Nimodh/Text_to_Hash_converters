import hashlib

def main():
    text = input("Type a text to convert it to hash_md5\n")
    hash_object = hashlib.md5(text.encode())
    md5_hash = hash_object.hexdigest()
    print(md5_hash)
    e= input()
    return

main()

