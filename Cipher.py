import random
import string

class cipher():
    def __init__(self):
        valid1 = False
        valid2 = False
        while(not valid1):
            print("Now running Matthew's Encryption Cipher.")
            choice1 = input("Type \"e\" to encrypt, Type \"d\" to decrypt.")
            if choice1 == "e":
                valid1 = True
                self.generate()
                print(self.keylist)
                while(not valid2):
                    choice2 = int(input("Please enter a number from 0-9 corresponding to the given keylist."))
                    if 0 <= choice2 <= 9:
                        valid2 = True
                        key = self.keylist[choice2]
                        plaintext = input("Please enter a plaintext message. The message should ONLY contain letters a-z and whitespaces.")
                        self.encrypt(key, plaintext)
                        raw1 = input("Press Enter to exit")
                    else:
                        print("Error! Please enter a valid input.")
            elif choice1 == "d":
                valid1 = True
                while (not valid2):
                    key = input("Please enter a decryption key of length 8 that ONLY contains letters a-z.")
                    if len(key) == 8:
                        valid2 = True
                        ciphertext = input(
                            "Please enter a ciphertext message. The message should ONLY contain letters a-z and whitespaces.")
                        self.decrypt(key, ciphertext)
                        raw2 = input("Press Enter to exit")
                    else:
                        print("Error! Please enter a valid input.")
            else:
                print("Error! Please enter a valid input.")

    def generate(self):
        alphabet = string.ascii_lowercase
        self.keylist = []
        for i in range(10):
            self.keylist.append(''.join(random.choice(alphabet) for j in range(8)))

    def encrypt(self, key, plaintext):
        alph = list("abcdefghijklmnopqrstuvwxyz ")
        keylist = list(key)
        plainlist = list(plaintext)
        numberedkeylist = self.textconvert(self.keymod(keylist, alph, plainlist), alph)
        numberedplaintext = self.textconvert(plainlist, alph)
        encrypted = []
        for i in range(len(numberedplaintext)):
            value = (numberedkeylist[i] + numberedplaintext[i]) % 27
            encrypted.append(value)
        print(''.join(self.numberconvert(encrypted, alph)))
    def decrypt(self, key, ciphertext):
        alph = list("abcdefghijklmnopqrstuvwxyz ")
        keylist = list(key)
        cipherlist = list(ciphertext)
        numberedkeylist = self.textconvert(self.keymod(keylist, alph, cipherlist), alph)
        numberedciphertext = self.textconvert(cipherlist, alph)
        encrypted = []
        for i in range(len(numberedciphertext)):
            value = (numberedciphertext[i] - numberedkeylist[i]) % 27
            encrypted.append(value)
        print(''.join(self.numberconvert(encrypted, alph)))

    def keymod(self, keylist, alph, plainlist):
        iterator = 0
        while len(keylist) < len(plainlist):
            keylist.append(keylist[iterator])
            keylist.append(alph[iterator])
            iterator += 1
            if iterator == 27:
                iterator = 0
        return keylist

    def textconvert(self, text, alph):
        numbered = []
        for i in range(len(text)):
            j = 0
            while j < len(alph):
                if text[i] == alph[j]:
                    numbered.append(j)
                    j = len(alph)
                j+=1
        return numbered

    def numberconvert(self, encryptedtext, alph):
        text = []
        for i in range(len(encryptedtext)):
            text.append(alph[encryptedtext[i]])
        return text

if __name__ == "__main__":
    cipher()