# dictionary where "A":0, "B":1, etc
from alphabet_dictionary import alphabet_dictionary
# python built in library to check if word exists
import enchant

# making a list of the keys and values for easy access in functions below
letters = list(alphabet_dictionary.keys())
numbers = list(alphabet_dictionary.values())

# dictionary used to check english words
english_dictionary = enchant.Dict("en_US")


def encrypt(message, key):
    try:
        key = int(key)
    except:
        print("The key provided is not a whole integer. Key: '" + key + "'")
        return
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
            shifted_char_position = get_shifted_char_position(shifted_num) 
            shifted_char = letters[shifted_char_position]
            encrypted_characters.append(shifted_char)

    encrypted_message = ''.join(encrypted_characters)
    return encrypted_message


def get_shifted_char_position(index):
    if index > 25:
        index = index % 26
    elif index < 0:
        while index < 0:
            index = index + 26

    return numbers.index(index)


def decrypt(message):
    # first split the message by spaces.
    # if each word has a different cipher value, then this is necessary.
    words = message.split(' ')
    list_of_results = []
    for word in words:
        results = check_all_shifts(word)
        list_of_results.append(results)
    return list_of_results


def check_all_shifts(encrypted_word):
    results = []
    for i in range(0,25):
        # since the process of decrypting is the same as encrypting, we can use the same function.
        decrypted_word = encrypt(encrypted_word, i)
        if english_dictionary.check(decrypted_word) == True:
            results.append(decrypted_word)
    return results


def print_results(encrypted_message, list_of_results):
    # list_of_results is a list of lists. First list is possibilities for the first word, etc
    words = encrypted_message.split(' ')
    i = 0
    for word in words:
        print("Potential Decryptions for '{0}': {1}".format(word, ', '.join(list_of_results[i])))
        i+=1


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
            if(encrypted_message is not None):
                print("Your encrypted message is: ")
                print(encrypted_message)
                prompt_user = False
        elif(choice == "D" or choice == "d"):
            print("Please enter the encrypted text.")
            print("Only letters and spaces may be entered.")
            message = input(">")
            results = decrypt(message)
            print_results(message, results)
        else:
            print("Invalid choice. Please enter E to encrypt or D to decrypt.")
            prompt_user = True

caeser_cipher()
