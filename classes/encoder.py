from bitarray import bitarray
import hashlib
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from PyQt6.QtGui import QPixmap, QImage, QColor
from classes.image import Image
import math

class Encoder:

    @staticmethod
    def encode(image, text:str, password:str):
        end_char = "ﬣ"

        hashed_p = Encoder._pass_to_hash(password)
        hashed_vi = Encoder._get_VI(password)
        encoded_text = Encoder._aes_encode_b(hashed_p.encode(), hashed_vi.encode(), text.encode())

        #encoding text with password before creating image
        encoded_text += end_char.encode()
        #print(encoded_text)
        #print(type(encoded_text))
        bit_text = Encoder._to_bitarr(encoded_text)


        max_bits_size = math.floor(math.sqrt((pow(image.image.width(), 2) + pow(image.image.height(), 2))))
        #print(max_bits_size)
        #print(len(bit_text))
        if min(image.image.width(), image.image.height()) < len(bit_text):
            print("Image is not big enough to encode that long text. Select bigger image")
            return False
        

        c = 0
        i = 0
        while c < len(bit_text):
            rgb_int_values = image.image.pixelColor(i,i).getRgb()
            rgb_new_int_values = []
            for j, color in enumerate(rgb_int_values):
                bit_color = Encoder._to_bitarr(bytes([color]))
                bit_color[-1] = bit_text[c+j]
                rgb_new_int_values.append(int.from_bytes(bit_color.tobytes()))
            
            new_qcolor = QColor(*tuple(rgb_new_int_values))
            image.image.setPixelColor(i, i, new_qcolor)

            c += len(rgb_int_values)
            i += 1

        image.image.save(image.name+"_crypted."+image.format, quality=100)

        ##decrypt test
#
        #coded_image = QImage(image.name+"_crypted."+image.format)
        #max_bits_size = math.floor(math.sqrt((pow(coded_image.width(), 2) + pow(coded_image.height(), 2))))
        #print(coded_image.width(), coded_image.height())
        #
        #gather_flag = True
#
        #i = 0
        #bits_arr = bitarray()
        #while gather_flag:
        #    rgb_int_values = coded_image.pixelColor(i,i).getRgb()
        #    for j, color in enumerate(rgb_int_values):
        #        bit_color = Encoder._to_bitarr(bytes([color]))
        #        #bits_arr += str(bit_color[-1])
        #        bits_arr.append(bit_color[-1])
        #    
        #        try:
        #            text_bits = bits_arr.tobytes()
        #            text_str = text_bits.decode()
        #            if text_str[-1] == end_char:
        #                print(text_str)
        #                gather_flag = False
        #        except: pass
        #    i += 1







        
        #rgb_int_values = image.pixelColor(0,0).getRgb()
        #print(rgb_int_values)
        #
        #print(rgb_bit_values)

    
    @staticmethod
    def encode_multiple(images:list, texts:list, password:str):
        pass

    @staticmethod
    def _pad(data:bytes) -> bytes:
        padding_length = 16 - len(data) % 16
        padding = bytes([padding_length] * padding_length)
        return data + padding
    
    @staticmethod
    def _pass_to_hash(password:str) -> str:
        hash_pass = hashlib.md5(password.encode()).hexdigest()
        return hash_pass

    @staticmethod
    def _get_VI(password:str) -> str:
        hash_vi = hashlib.blake2s(str(len(password)).encode(), digest_size=8).hexdigest()
        return hash_vi

    @staticmethod
    def _aes_encode_b(key:bytes, vi:bytes, text:bytes) -> bytes:
        
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
    def _aes_encode_s(key:str, vi:str, text:str) -> bytes:

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

    @staticmethod
    def _to_bits(data:bytes) -> str:
        return ''.join([format(b, '08b') for b in data])

    @staticmethod
    def _to_bitarr(data:bytes) -> bitarray:
        ba = bitarray()
        ba.frombytes(data)
        return ba