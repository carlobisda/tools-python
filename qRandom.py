# NAME: qRandom
# VERSION: 1.0.0
# LICENSE: MIT
# AUTHOR: Carlo Bisda
# NOTES: A command line randomizer which takes data from a file of choice and it will output an anwer
# SYNTAX: qrandom (filename.???) 
import random
import sys
import os

def select_random(filename):
    if os.path.exists(filename): #CHECKS IF INPUT FILE EXISTS
        with open(filename, 'r') as f:
            titles = f.readlines()
            return random.choice(titles).strip()

    else:
        return "File Not Found."

if __name__ == '__main__':
    if len(sys.argv) > 1: #PASSES COMMAND LINE ARGUMENTS TO THE SCRIPT
        filename = sys.argv[1] #FILENAME VARIABLE
    else:
        filename = 'choice.txt' #DEFAULT FILE

    print(select_random(filename))