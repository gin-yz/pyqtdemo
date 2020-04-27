import os
from binascii import b2a_hex

from Crypto.Cipher import AES
import random, string
from secretsharing import PlaintextToHexSecretSharer
from ecies import encrypt


class PrpCrypt(object):

    def __init__(self, key, offset):
        self.key = key.encode()
        self.offset = offset.encode()
        self.mode = AES.MODE_CBC

    def encrypt(self, text):
        cryptor = AES.new(self.key, self.mode, self.offset)
        length = 16
        count = len(text)
        if count < length:
            add = (length - count)
            text = text + ('\0'.encode() * add)
        elif count > length:
            add = (length - (count % length))
            text = text + ('\0'.encode() * add)
        self.ciphertext = cryptor.encrypt(text)
        return self.ciphertext

    def decrypt(self, text):
        cryptor = AES.new(self.key, self.mode, self.offset)
        plain_text = cryptor.decrypt(text)
        return plain_text.rstrip('\0'.encode())


def encrypt_run(path):
    # aes加密
    tmpkey = random.sample(string.ascii_letters + string.digits, 16)
    tmpoffset = random.sample(string.ascii_letters + string.digits, 16)
    key = ''.join(tmpkey)
    offset = ''.join(tmpoffset)
    # print(key,offset)
    name, suffix = os.path.splitext(path)
    pc = PrpCrypt(key, offset)
    with open(path, 'rb') as file_object:
        contents = file_object.read()
        e = pc.encrypt(contents)
    with open(name + '.copyright', 'wb') as file_object:
        file_object.write((suffix + '\n').encode())
        file_object.write(e)

    # 分割
    shares = PlaintextToHexSecretSharer.split_secret(key + offset, 3, 5)

    # sharesstr = ','.join(shares)

    # print('分割',sharesstr)
    encrypt_list = []
    public_list  = [
        '0xc31656b66cf4e8d8584e35f7318d3e7cc2d7820768b7683b2057b714e383e2678108126f29ce42aa6a7010ef6d60581431972010ff517f571a21c8b74f42857c',
        '0x8a3d49ede094a68158d8f2be4d5eb816e9a20280f45ca7a3b5205fefc6475b8cc34014524fe78e71636bb26fdc47dc44da548538e43d0ea790a9fd0f5d558483',
        '0x1eba8ab60e0a7b99e0bdfb67ddbea8bb8b5a5d37e339b3210c2ce320e05d8000023bc6a8027de24b4cf80d1cc7ba28a71fcb6a06bb69ee4019d418f342c71f79',
        '0x0cb1b0db1af57669e8b5506daa7b5c873ab51165aef47836717ec6f439086fd118a07fafd35c1b75b4050fdf6d0bae911d10722f6dbe24dfe340a43fa6bf3cee',
        '0xdbe48fe7fa695231e6bdbb09ed6d9eb4431554c85f846223414890e2fdd1ab0f761b58039f5a2ea4a16d1c235d11a69ffd107533fae63139e1159c5c58c89081'
    ]
    for public,share in zip(public_list,shares):
        encrypt_list.append(b2a_hex(encrypt(public, share.encode())).decode())
    # print(encrypt_list)
    encrypt_str = ','.join(encrypt_list)
    # print(encrypt_str)
    with open(name + '.key', 'wb') as f:
        f.write(encrypt_str.encode())

    return (True, name)
