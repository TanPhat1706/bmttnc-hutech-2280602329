import hashlib

def calculate_sha256(input_string):
    sha256_hash = hashlib.sha256()
    sha256_hash.update(input_string.encode('utf-8'))
    return sha256_hash.hexdigest()

data_to_hash = input("Nhập chuỗi cần băm: ")
hash_value = calculate_sha256(data_to_hash)
print(f"Giá trị hash SHA-256 của chuỗi '{data_to_hash}' là: {hash_value}")