from bitarray import bitarray
import hashlib
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

class Decoder:

    @staticmethod
    def decode(image, password):
        pass
    
    @staticmethod
    def decode_multiple(images:list, password:str):
        pass

    @staticmethod
    def _unpad(data:bytes) -> bytes:
        padding_length = data[-1]
        if padding_length < 1 or padding_length > 16:
            raise ValueError("Invalid padding encountered")
        return data[:-padding_length]

    @staticmethod
    def _aes_decode_b(key:bytes, vi:bytes, text:bytes) -> str:

        cipher = Cipher(algorithms.AES(key), modes.CBC(vi))
        decryptor = cipher.decryptor()
        decoded_text = decryptor.update(text) + decryptor.finalize()

        output_str = Decoder._unpad(decoded_text)

        return output_str.decode("utf-8")

    @staticmethod
    def _from_bits(data:str) -> bytes:
        data_to_cut = data
        bytes_tab = []
        print(len(data))
        print(len(data) % 8 == 0)
        while len(data_to_cut) > 0 and len(data_to_cut) % 8 == 0:
            bytes_tab.append(data_to_cut[:8])
            data_to_cut = data_to_cut[8:]

        print(bytes_tab)

        return bytes()

    @staticmethod
    def _from_bitarr(data:bitarray) -> bytes:
        return data.tobytes()
