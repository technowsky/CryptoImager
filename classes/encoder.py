from bitarray import bitarray
import hashlib
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from PyQt6.QtGui import QColor
from PyQt6.QtCore import Qt, QEventLoop
from classes.image import Image
import math
from classes import settingManager
from classes.widgets.askForName import askWin
from classes import settingManager


class Encoder:

    @staticmethod
    def encode(image:Image, text:str, password:str):
        end_char = "ﬣ"

        
        #print(end_char.encode())

        hashed_p = Encoder._pass_to_hash(password)
        hashed_vi = Encoder._get_VI(password)
        encoded_text = Encoder._aes_encode_b(hashed_p.encode(), hashed_vi.encode(), text.encode())


        #encoding text with password before creating image
        encoded_text += end_char.encode()
        #print(encoded_text.decode())
        #print(type(encoded_text))
        #print(encoded_text)
        #print(hashed_p)
        #print(hashed_vi)

        bit_text = Encoder._to_bitarr(encoded_text)
        #print(len(bit_text))
        #print(bit_text)
        code_number = settingManager.get_setting("coding_method")
        
        c_image = None

        if(code_number == 0): c_image = Encoder._code_diagonaly(image, bit_text)
        elif(code_number == 1): c_image = Encoder._code_first_to_last(image, bit_text)
        elif(code_number == 2): ...




        #print(bits_arr)
        Encoder._save_image(c_image)
    
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
    
    @staticmethod
    def _save_image(image: Image) -> None: 
        encoded_image_name = image.name+"."+image.format

        if settingManager.current_json_settings.get("save_custom_name") == 0:    #global
            encoded_image_name = settingManager.current_json_settings.get("save_prefix")+"_"+encoded_image_name
        elif settingManager.current_json_settings.get("save_custom_name") == 1:  #ask every time
            ask_window = askWin()
            ask_window.exec()
            encoded_image_name = ask_window.name_input_text+"."+image.format

        image.image.save(settingManager.current_json_settings.get("save_dir")+encoded_image_name, quality=100)

    @staticmethod
    def _code_diagonaly(image: Image, bit_text: bitarray) -> Image:
        coding_flag = True

        if min(image.image.width(), image.image.height())*3 < len(bit_text):
            print("Image is not big enough to encode that long text. Select bigger image")
            return False
        

        c = 0
        i = 0
        #print(bit_text)
        bits_arr = bitarray()

        while coding_flag:
            #print(bit_text)
            rgb_int_values = image.image.pixelColor(i,i).getRgb()[:3]
            #print(rgb_int_values)
            rgb_new_int_values = list(rgb_int_values)
            for j, color in enumerate(rgb_new_int_values):
                #print(color)
                #print(type(color))
                bit_color = Encoder._to_bitarr(bytes([color]))
                #print(bit_text[c+j])
                bit_color[-1] = bit_text[c]
                bits_arr.append(bit_text[c])
                rgb_new_int_values[j] = int(bit_color.to01(), 2)
                #del bit_text[0]
                c += 1
                if c == len(bit_text):
                    coding_flag = False
                    break
                
            new_qcolor = QColor(*tuple(rgb_new_int_values))
            image.image.setPixelColor(i, i, new_qcolor)

            i += 1

        return image
    

    @staticmethod
    def _code_first_to_last(image: Image, bit_text: bitarray) -> Image: # have to create first to last coding function
        coding_flag = True

        if (image.image.width()*image.image.height())*3 < len(bit_text):
            print("Image is not big enough to encode that long text. Select bigger image")
            return False
        

        c = 0

        row = 0
        column = 0
        #print(bit_text)
        bits_arr = bitarray()

        while coding_flag:
            #print(bit_text)
            rgb_int_values = image.image.pixelColor(row,column).getRgb()[:3]
            #print(rgb_int_values)
            rgb_new_int_values = list(rgb_int_values)
            for j, color in enumerate(rgb_new_int_values):
                #print(color)
                #print(type(color))
                bit_color = Encoder._to_bitarr(bytes([color]))
                #print(bit_text[c+j])
                bit_color[-1] = bit_text[c]
                bits_arr.append(bit_text[c])
                rgb_new_int_values[j] = int(bit_color.to01(), 2)
                #del bit_text[0]
                c += 1
                if c == len(bit_text):
                    coding_flag = False
                    break
                
            new_qcolor = QColor(*tuple(rgb_new_int_values))
            image.image.setPixelColor(row, column, new_qcolor)

            
            if(column == image.image.width()):
                column = 0
                row += 1
            else: column += 1 


        return image