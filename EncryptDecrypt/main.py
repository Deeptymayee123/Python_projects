#Using caesar cipher method

letters = 'abcdefghijklmnopqrstuvwxyz'
num_letters = len(letters)

#key = 3
#g--> j

def Encryptdecrypt(text, mode, key):
    restext = ''
    for letter in text:
        letter = letter.lower()

        if not letter == ' ':
             index = letters.find(letter)
             if index == -1:
                # added the exact letter if it is a special char
                 restext += letter  
             else:
                 if(mode == 'e'):
                     new_index = index + key
                     if new_index >= num_letters:
                        new_index -=  num_letters
                     restext += letters[new_index]
                 else:
                     new_index = index - key
                     if new_index < 0:
                       new_index +=  num_letters
                     restext += letters[new_index]
    return restext
# def encrypt(plaintext, Key):
#     ciphertext = ''
#     for letter in plaintext:
#         letter = letter.lower()
#         if not letter == ' ':
#              index = letters.find(letter)
#              if index == -1:
#                 #  added the exact letter if it is a special char
#                  ciphertext += letter  
#              else:
#                  new_index = index + key
#                  if new_index >= num_letters:
#                      new_index -=  num_letters
#                  ciphertext += letters[new_index]
                     
#     return ciphertext

# def decrypt(ciphertext, Key):
#     plaintext = ''
#     for letter in ciphertext:
#         letter = letter.lower()
#         if not letter == ' ':
#              index = letters.find(letter)
#              if index == -1:
#                 #  added the exact letter if it is a special char
#                  plaintext += letter  
#              else:
#                  new_index = index - key
#                  if new_index < 0:
#                      new_index -=  num_letters
#                  plaintext += letters[new_index]
                     
#     return plaintext



print("CEASAR CIPHER PROGRAM")
print()

print("Do you want to encrypt or decrypt")
user_input = input('e/d: ').lower()
print()

if user_input == 'e':
    print('ENCRIPTION MODE SELECTED')
    print()
    key = int(input('Enter the key (1 through 26): '))
    text = input('Enter the text to encrypt: ')
    ciphertxt = Encryptdecrypt(text, user_input, key)
    print(f'ciphertext: {ciphertxt}')
else:
  if user_input == 'd':
    print('DECRIPTION MODE SELECTED')
    print()
    key = int(input('Enter the key (1 through 26): '))
    text = input('Enter the text to decrypt: ')
    plaintxt = Encryptdecrypt(text, user_input, key)
    print(f'plaintxt: {plaintxt}')       
    
