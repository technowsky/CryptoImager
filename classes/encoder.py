import hashlib
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

class Encoder:

    @staticmethod
    def encode(image, text, password):
        pass
    
    @staticmethod
    def encode(images:list, texts:list, password):
        pass

    @staticmethod
    def _pad(data:bytes):
        padding_length = 16 - len(data) % 16
        padding = bytes([padding_length] * padding_length)
        return data + padding

    @staticmethod
    def _unpad(data:bytes):
        padding_length = data[-1]
        if padding_length < 1 or padding_length > 16:
            raise ValueError("Invalid padding encountered")
        return data[:-padding_length]
    
    @staticmethod
    def _pass_to_hash(password):
        hash_pass = hashlib.md5(password.encode()).hexdigest()
        return hash_pass

    @staticmethod
    def _get_VI(password):
        hash_vi = hashlib.blake2s(str(len(password)).encode(), digest_size=8).hexdigest()
        return hash_vi

    @staticmethod
    def _aes_encode(key:bytes, vi:bytes, text:bytes):
        
        #print(len(''.join(f'{z:08b}' for z in key.encode())))
        #print(len(''.join(f'{z:08b}' for z in vi.encode())))
        text = Encoder._pad(text)

        cipher = Cipher(algorithms.AES(key), modes.CBC(vi))
        encryptor = cipher.encryptor()
        encoded_text = encryptor.update(text) + encryptor.finalize()

        return encoded_text
        #decryptor = cipher.decryptor()
        #decoded_text = decryptor.update(encoded_text) + decryptor.finalize()
#
#
        #print(Encoder._unpad(decoded_text))
#
    @staticmethod
    def _aes_encode(key:str, vi:str, text:str):

        b_key = key.encode()
        b_vi = vi.encode()
        b_text = text.encode()
        
        #print(len(''.join(f'{z:08b}' for z in key.encode())))
        #print(len(''.join(f'{z:08b}' for z in vi.encode())))
        b_text = Encoder._pad(b_text)

        cipher = Cipher(algorithms.AES(b_key), modes.CBC(b_vi))
        encryptor = cipher.encryptor()
        encoded_text = encryptor.update(b_text) + encryptor.finalize()

        return encoded_text