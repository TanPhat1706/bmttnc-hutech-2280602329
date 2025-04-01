import rsa, os

class RSACipher:
    def __init__(self):
        self.private_key = None
        self.public_key = None
        self.key_dir = 'cipher/rsa/keys'
        if not os.path.exists(self.key_dir):
            os.makedirs(self.key_dir)

    def generate_keys(self):
        self.public_key, self.private_key = rsa.newkeys(512)
        self.save_keys()

    def save_keys(self):
        with open(os.path.join(self.key_dir, "private.pem"), "wb") as priv_file:
            priv_file.write(self.private_key.save_pkcs1())
        
        with open(os.path.join(self.key_dir, "public.pem"), "wb") as pub_file:
            pub_file.write(self.public_key.save_pkcs1())

    def load_keys(self):
        with open(os.path.join(self.key_dir, "private.pem"), "rb") as priv_file:
            private_key = rsa.PrivateKey.load_pkcs1(priv_file.read())
        
        with open(os.path.join(self.key_dir, "public.pem"), "rb") as pub_file:
            public_key = rsa.PublicKey.load_pkcs1(pub_file.read())
        return private_key, public_key

    def encrypt(self, message, key):
        return rsa.encrypt(message.encode(), key)

    def decrypt(self, ciphertext, key):
        return rsa.decrypt(ciphertext, key).decode()

    def sign(self, message, private_key):
        return rsa.sign(message.encode(), private_key, 'SHA-1')

    def verify(self, message, signature, public_key):
        try:
            return rsa.verify(message.encode(), signature, public_key) == 'SHA-1'
        except:
            return False
