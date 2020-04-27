import os

from ecies import decrypt
from secretsharing import PlaintextToHexSecretSharer
from encryptmodule import PrpCrypt
from binascii import b2a_hex, a2b_hex

def decrypt_run(copyright, key, private):
    # 恢复aes密钥
    with open(key, 'rb') as file_object:
        contents = file_object.read()
        print(contents)
        # print(contents.split(b'\n', 1))
    # contents_list = contents.split(b'\n', 1)
    # suffix = contents_list[0]
    # print(private,type(private))
    # list = decrypt(str(private), contents).decode().split(',')
    en_list = contents.decode().split(',')
    # print(en_list)
    # print(private)
    # print(decrypt(str(private),a2b_hex(en_list[0].encode())).decode())
    # print(decrypt(str(private), a2b_hex(en_list[1].encode())).decode())
    # print(decrypt(str(private), a2b_hex(en_list[2].encode())).decode())
    de_list = [decrypt(str(private),a2b_hex(x.encode())).decode() for x in en_list]
    # print(de_list)
    aes_str = PlaintextToHexSecretSharer.recover_secret(de_list)
    # print(aes_str)
    key = aes_str[0:16]
    offset = aes_str[16:32]
    # print(key,offset)

    # aes解密
    name, _ = os.path.splitext(copyright)
    pc = PrpCrypt(str(key), str(offset))
    with open(copyright, 'rb') as file_object:
        contents = file_object.read()
        contents_list = contents.split(b'\n', 1)
        suffix = contents_list[0]
        e = pc.decrypt(contents_list[1])
    with open(name + suffix.decode(), 'wb') as file_object:
        file_object.write(e)

    return True, name + suffix.decode()
