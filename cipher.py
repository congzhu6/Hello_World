"""
This module aims to break Caesar-ciphers from German plaintext
based     on statistics of letter distribution.

The caesar cipher is a character substitution algorithm.
Bob chooses a number as the key n.
Bob then shifts every character of the plain-text by n, cycling  
through the entire alphabet.

e.g.: if n = 3: "ABC" -> "DEF".

Since it has a very small keyspace (26^1), it can be easily broken, 
and Mallory could even guess or bruteforce the key.
(Note: You could choose a number higher than 26. However, this won't 
increase your keyspace since any number x will
be reduced to 1-26. See: (x - (26*(x // 26)).

Common letters in the german language are (in descending order):
"E","N","I","S","R" (subject to verification)

The statistical approach works well for long sentences since one has 
a greater samplesize for distribution analysis.
If two or more letters appear the same amount of times, you have to 
check which key is actually correct, either
by simply reading the outputs or running them against a 
distribution_dict of that language.

"""

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
SPECIAL_CHARS = " ,.-;:_?!="

# def encrypt(plain_text, key):
#     """
#     Encrypts plaintext using a caesar.

#     :param plain_text:  The plaintext
#     :param key: The key (Integer)
#     :return: The cipher-text
#     """
#     cipher_text = ""
#     for letter in plain_text:
#         if letter in SPECIAL_CHARS:
#             cipher_text += letter
#             continue
#         index = ALPHABET.find(letter.upper())
#         new_index = flatten(index + key)
#         cipher_text += ALPHABET[new_index]
#     return cipher_text

def decrypt(cipher_text, key=None):
    """
    This function decrypts plaintext. If no key is specified, it 
    will be found using distribution analysis.
    :param cipher_text: The cipher-text
    :param key: The key
    :return: the plain-text
    """
    if key is None:
        key = find_key_from_cipher(cipher_text)

    plain_text = ""
    for letter in cipher_text:
        
        index = ALPHABET.find(letter.upper())
        new_index = flatten(index - key)
        plain_text += ALPHABET[new_index]

    return plain_text

def flatten(number) :
    """
    Flattens the key back to be in range(1,26)
    :param number: 
    :return: 
    """
    return number - (26*(number//26))


def find_key_from_cipher(cipher_text):
    index_of_most_common_letter = 4 #Index of 'e'

    #Calculate distribution
    distribution_dict = analyse_letter_distribution(cipher_text)
    #Get common letters
    common_letters = sorted(distribution_dict, key=distribution_dict.get, reverse=True)

    #Use most common letter to get key
    key = ALPHABET.find(common_letters[0].upper()) - index_of_most_common_letter
    return key

def analyse_letter_distribution(cipher_text):
    distribution_dict = {}
    for letter in cipher_text:
        
        if letter not in distribution_dict:
            distribution_dict[letter] = 1
        else:
            distribution_dict[letter] += 1
    # if len(distribution_dict.values()) != len(distribution_dict.values()):
    #     print("Multiple letters appear the same amount of times! Uh oh.")
    return distribution_dict

    # if __name__ == "__main__":
    #     secret = encrypt("This sentence is encrypted. Encryption is broken     by using awesome encryption algorithms!",5)
    #     print(decrypt(secret))
print(decrypt('ycvejqwvhqtdtwvwu'))