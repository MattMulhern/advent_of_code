#!/usr/bin/python3
# import hashlib
import re
import subprocess


def get_md5(checkstr):
    command = "echo {0} | md5sum".format(checkstr)
    proc = subprocess.getoutput(command).strip(' -')
    return proc


def find_five_zero_hash(input):
    for line in input:
        check        = True
        num_to_check = 0
        while check:
            num_to_check += 1
            str_to_check = "{0}{1}".format(line.strip(), num_to_check).encode('utf-8')
            # md5 = hashlib.md5(str_to_check).hexdigest()
            md5 = get_md5(str_to_check)
            if re.match('^00000.*', md5):
                print("MATCHING HASH!", num_to_check, "=>", str_to_check, ":", md5)
                check = False

            print(num_to_check, "=>", str_to_check, ":", md5)
if __name__ == '__main__':
    input = open('./input.txt', 'r').readlines()
    find_five_zero_hash(input)
