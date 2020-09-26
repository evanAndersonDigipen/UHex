import codecs
from os import system

def decodeHex():
    system('cls')
    print("Mode Set to Decode \n")
    hexIn = bytes(input("Enter Hex without 0x or spaces: "), encoding='utf-8')
    print("\n")

    print(codecs.decode(hexIn, encoding='hex'))
def encodeHex():
    system('cls')
    print("Mode Set to Encode\n")
    phraseIn = input("Enter the Phrase you want to be converted into hex: ")
    phraseIn = ''.join([hex(ord(x)) for x in phraseIn])
    print('\n')
    OX = input("Would you like it with 0x? y/n: ")
    if OX in ['Y', 'y', 'Yes', 'yes']:
        phraseIn = ''.join(phraseIn[i: i+4] for i in range(0, len(phraseIn), 4))
        print(phraseIn)
    elif OX in ['N', 'n', 'No', 'no']:
        print(phraseIn.replace('0x', ''))
    else:
        print("That is not a valid input \n")
        encodeHex()
def main():
    mode = input("Enter Decode or Encode: ")
    deCode = ["d", "D", "Decode", "decode"]
    enCode = ["e", "E", "Encode", "encode"]
    if mode in deCode:
        decodeHex()
    elif mode in enCode:
        encodeHex()
    else:
        print("You did not select a valid mode, please try again \n")
        main()

main()