import hashlib

def blake2(message):
    blake2_hash = hashlib.blake2b(digest_size=64)
    blake2_hash.update(message.encode('utf-8'))
    return blake2_hash.hexdigest()

def main():
    input_string = input("Nhập chuỗi cần băm: ")
    blake2_hash = blake2(input_string)
    print(f"Mã băm BLAKE2 của chuỗi '{input_string}' là: {blake2_hash}")
    
if __name__ == "__main__":
    main()