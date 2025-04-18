from bitarray import bitarray
import hashlib
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import math
from classes.encoder import *

class Decoder:

    @staticmethod
    def decode(coded_image, password:str):
        end_char = "ﬣ"
        max_bits_size = math.floor(math.sqrt((pow(coded_image.width(), 2) + pow(coded_image.height(), 2))))
        print(coded_image.width(), coded_image.height())
        
        gather_flag = True

        i = 0
        bits_arr = bitarray()
        while gather_flag and i < min(coded_image.width(), coded_image.height()):
            rgb_int_values = coded_image.pixelColor(i,i).getRgb()
            for j, color in enumerate(rgb_int_values):
                bit_color = Encoder._to_bitarr(bytes([color]))
                #bits_arr += str(bit_color[-1])
                bits_arr.append(bit_color[-1])
            
                try:
                    text_bits = bits_arr.tobytes()
                    text_str = text_bits.decode()
                    #print(text_str)
                    if text_str[-1] == end_char:
                        #print(text_str)
                        gather_flag = False
                except: pass
            i += 1

        print(bits_arr.tobytes())

    
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
        while len(data_to_cut) > 0 and len(data_to_cut) % 8 == 0:
            bytes_tab.append(data_to_cut[:8])
            data_to_cut = data_to_cut[8:]

        print(bytes_tab)

        return bytes()

    @staticmethod
    def _from_bitarr(data:bitarray) -> bytes:
        return data.tobytes()
