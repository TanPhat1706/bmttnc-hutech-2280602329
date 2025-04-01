from Crypto.Hash import SHA3_256

def sha3(message):
    sha3_hash = SHA3_256.new()
    sha3_hash.update(message.encode('utf-8'))
    return sha3_hash.hexdigest()

def main():
    input_string = input("Nhập chuỗi cần băm: ")
    sha3_hash = sha3(input_string)
    print(f"Mã băm SHA-3 của chuỗi '{input_string}' là: {sha3_hash}")
    
if __name__ == "__main__":
    main()