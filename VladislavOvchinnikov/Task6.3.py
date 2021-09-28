import itertools
import string


class Cipher:

    def __init__(self, keyword):
        self.keyword = keyword
        self.standart_alphabet = list(string.ascii_uppercase)
        self.crypto_alphabet = list(''.join(c[0] for c in itertools.groupby(self.keyword)).upper())
        for char in string.ascii_uppercase:
            if char in self.crypto_alphabet:
                continue
            else:
                self.crypto_alphabet.append(char)

    def encode(self, word: str) -> str:
        encrypted_word = ""
        for char in word:
            if char.upper() in self.standart_alphabet:
                index = self.standart_alphabet.index(char.upper())
            else:
                encrypted_word += char
                continue
            encrypted_word += self.crypto_alphabet[index]
        return encrypted_word

    def decode(self, word: str) -> str:
        decoded_word = ""
        for char in word:
            if char.upper() in self.crypto_alphabet:
                index = self.crypto_alphabet.index(char.upper())
            else:
                decoded_word += char
                continue
            decoded_word += self.standart_alphabet[index]
        return decoded_word


cipher = Cipher("cryyyyypto")
print(cipher.standart_alphabet)
print(cipher.crypto_alphabet)
print(cipher.encode("Hello world"))
print(cipher.decode("Fjedhc dn atidsn"))
