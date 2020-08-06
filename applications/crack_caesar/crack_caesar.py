# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

from os.path import dirname, join

current_dir = dirname(__file__)
file_path = join(current_dir, "./ciphertext.txt")
with open(file_path, 'r') as f:
    cipher_text = f.read()

letter_count = {}
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

cipher_text = cipher_text.upper()

for character in cipher_text:
    if character in letters:
        if character not in letter_count.keys():
            letter_count[character] = 1
        else:
            letter_count[character] += 1

sorted_letter_count = list(letter_count.items())
sorted_letter_count.sort(key=lambda x: x[1], reverse=True)

sorted_letters  = "".join([pair[0] for pair in sorted_letter_count])

eng_frequency = "ETAOHNRISDLWUGFBMYCPKVQJXZ"

decode_cipher = dict(zip(sorted_letters, eng_frequency))

def crack_caesar(str):
    decoded_cipher = ""
    for character in str:
        if character in letters:
            decoded_cipher += decode_cipher[character]
        else:
            decoded_cipher += character
    return decoded_cipher

print(crack_caesar(cipher_text))