#Name: qPassword Generator
#Author: Carlo Bisda
#Version: 1.0.0
#License: MIT

import random
import string

def gen_pass(length):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for i in range(length))
    return password

if __name__ == '__main__':
    password = gen_pass(12)
    print(password)