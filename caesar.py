# dictionary where "A":0, "B":1, etc
from alphabet_dictionary import alphabet_dictionary

# making a list of the keys and values for easy access in functions below
letters = list(alphabet_dictionary.keys())
numbers = list(alphabet_dictionary.values())

def encrypt(message, key):
    try:
        key = int(key)
    except:
        print("The key provided is not a whole integer. Key: '" + key + "'")
    encrypted_characters = []
    characters = list(message)
    for char in characters:
        # first check if it's just a space.
        if char == ' ':
            encrypted_characters.append(' ')
        # if it's not a space, confirm it is a letter and that it is 
        # in the dictionary (doesn't have an accent).
        elif char.isalpha() == False or char.upper() not in letters:
            print("Only letters and spaces are accepted. Unable to encrypt '" + char + "'")
            return
        else:
            char = char.upper()
            num = alphabet_dictionary[char]
            shifted_num = num + key
            shifted_char_position = numbers.index(shifted_num)
            shifted_char = letters[shifted_char_position]
            encrypted_characters.append(shifted_char)

    encrypted_message = ''.join(encrypted_characters)
    return encrypted_message







def caeser_cipher():
    prompt_user = True
    while(prompt_user):
        choice = input("Would you like to Encrypt or Decrypt? Enter E or D.")
        if(choice == "E" or choice == "e"):
            print("Please enter your message to encrypt.")
            print("Only letters and spaces may be entered.")
            message = input(">")
            print("Please enter the key, or the number of letters to shift the message by.")
            print("Only whole integers are accepted.")
            key = input(">")
            encrypted_message = encrypt(message,key)
            print("Your encrypted message is: ")
            print(encrypted_message)
            prompt_user = False
        elif(choice == "D" or choice == "d"):
            print("decyrpting...")
            prompt_user = False
        else:
            print("Invalid choice. Please enter E to encrypt or D to decrypt.")
            prompt_user = True


caeser_cipher()