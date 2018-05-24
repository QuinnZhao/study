import time
import random
import hashlib

__author__ = 'Quinn Zhao'

# Thanks Slwhy

def salt_sign_generator(text):
    salt = str(int(time.time()*1000)+random.randint(1,10)) # 生成时间戳 i
    client = 'fanyideskweb' # u
    d = 'aNPG!!u6sesA>hBAW1@(-'  #'ebSeFb%=XZ%T[KZ)c(sy!' l
    m5= hashlib.md5()
    src = client + text + salt + d
    m5.update(src.encode('utf-8'))
    sign = m5.hexdigest()

    return salt, sign


if __name__ == '__main__':
    print(salt_sign_generator('face'))
