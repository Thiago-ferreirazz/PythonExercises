def caeser(message, shift):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ""
    
    for char in message.lower():

        if not char.isalpha():
            final_message += char
        else:
            new_index = alphabet.find(char)
            new_char = alphabet[(new_index + shift)%26]
            final_message += new_char
    
    return final_message

def vigenere(message, key, direction = 1):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ""
    key_index = 0
    
    for char in message.lower():

        if not char.isalpha():
            final_message += char
        else:

            key_char = key[key_index %len(key)]
            key_index += 1


            new_index = alphabet.find(char)
            offset = alphabet.index(key_char)
            new_char = alphabet[(new_index + offset * direction)%26]
            final_message += new_char
    
    return final_message


