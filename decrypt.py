ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def decrypt(cipher_text, key=None):
    
    if key is None:
        key = find_key(cipher_text)

    plain_text = ""
    for letter in cipher_text:
        
        index = ALPHABET.find(letter.upper())
        new_index = flatten(index - key)
        plain_text += ALPHABET[new_index]

    return plain_text

def flatten(number) :
    
    return number - (26*(number//26))


def find_key(cipher_text):
    index_of_most_common_letter = 4 

    #Calculate distribution
    distribution_dict = analyse(cipher_text)
    #Get common letters
    common_letters = sorted(distribution_dict, key=distribution_dict.get, reverse=True)

    #Use most common letter to get key
    key = ALPHABET.find(common_letters[0].upper()) - index_of_most_common_letter
    return key

def analyse(cipher_text):
    distribution_dict = {}
    for letter in cipher_text:
        
        if letter not in distribution_dict:
            distribution_dict[letter] = 1
        else:
            distribution_dict[letter] += 1
    return distribution_dict

    

print(decrypt('ycvejqwvhqtdtwvwu'))