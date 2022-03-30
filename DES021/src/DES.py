#! py -3
# encoding:utf-8

from Cryptodome.Cipher import DES

import binascii

# DES加密数据的长度须为8的倍数，不够可以用其它字符填充
text = '20191042021'
if len(text) % 8 != 0:
    text = text + " " * (8 - len(text) % 8)
# 密钥：必须为8字节
key = b'91042021'
# 使用 key 初始化 DES 对象，使用 DES.MODE_ECB 模式
des = DES.new(key, DES.MODE_ECB)
# 加密
result = des.encrypt(text.encode())

print('加密后的数据：', result)
# 转为十六进制    binascii 的 b2a_hex 或者 hexlify 方法
print('转为十六进制：', binascii.b2a_hex(result))
# 解密
print('解密后的数据：', des.decrypt(result).decode('utf-8'))