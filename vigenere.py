def caeser(message, shift):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ""

     # Append any non-letter character to the message
    for char in message.lower():

        if not char.isalpha():
            final_message += char
        else:
            # Define the encrypted letter
            new_index = alphabet.find(char)
            new_char = alphabet[(new_index + shift)%26]
            final_message += new_char
    
    return final_message


def vigenere(message, key, direction=1):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ""
    key_index = 0
    key = key.lower()  
    
    for char in message.lower():
         # Append any non-letter character to the message
        if not char.isalpha():
            final_message += char
        else:
            # Find the right key character to encode/decode
            key_char = key[key_index % len(key)]
            key_index += 1
            
           # Define the offset and the encrypted/decrypted letter
            char_index = alphabet.find(char)
            key_offset = alphabet.find(key_char)
            
       
            new_index = (char_index + key_offset * direction) % len(alphabet)
            final_message += alphabet[new_index]
    
    return final_message


# Tests
encrypted = vigenere("arroz", "batata")
print("Criptografado:", encrypted)
decrypted = vigenere(encrypted, "batata", -1)
print("Descriptografado:", decrypted)

