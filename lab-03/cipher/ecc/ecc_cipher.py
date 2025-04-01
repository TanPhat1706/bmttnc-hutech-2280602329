import ecdsa, os

if not os.path.exists('cipher/ecc/keys'):
    os.makedirs('cipher/ecc/keys')

class ECCCipher:
    def __init__(self):
        pass
    
    def generate_keys(self):
        sk = ecdsa.SigningKey.generate()
        vk = sk.get_verifying_key()
        
        with open('cipher/ecc/keys/private.pem', 'wb') as f:
            f.write(sk.to_pem())
        
        with open('cipher/ecc/keys/public.pem', 'wb') as f:
            f.write(vk.to_pem())
    
    def load_keys(self):
        with open('cipher/ecc/keys/private.pem', 'rb') as f:
            sk = ecdsa.SigningKey.from_pem(f.read())
        
        with open('cipher/ecc/keys/public.pem', 'rb') as f:
            vk = ecdsa.VerifyingKey.from_pem(f.read())
        
        return sk, vk
    
    def sign(self, message, sk):
        return sk.sign(message.encode('ascii'))
    
    def verify(self, message, signature, vk):
        _, vk = self.load_keys()
        try:
            return vk.verify(signature, message.encode('ascii'))
        except ecdsa.BadSignatureError:
            return False