import random
import string

def shift(current_position, distance, direction: 0,):
    direction = 1 if direction else -1
    return current_position + direction * distance


def stream_cipher(message, key, do_encrypt=True):
    """
    This function will receive a message, a key, and the
    decision to encrypt or decrypt the message.
    The function uses a stream cipher encryption algorithm 
    which replaces each letter in the message with a 
    pseudo-random character from a given character set.
    Example:
    >>> stream_cipher("This is a test", 1234)
    'wPwV~#5;:D"905'
    >>> stream_cipher('wPwV~#5;:D"905', 1234, False)
    'This is a test'
    """
    random.seed(key)
    # The character set must be multiplied by 2 so
    # a character shifted beyond the end of the 
    # character set will loop back to the beginning.
    characters = 2 * (
                      string.ascii_letters +
                      string.digits +
                      string.punctuation + ' '
                     )
    # I declare this in a variable so the 
    # program can work with a variable length character set
    lenchars = len(characters)//2
    # This will replace each character in the message
    # with a pseudo-random character selected from
    # the character set.
    return ''.join([characters[shift(characters.index(message[each_char]), lenchars - int(lenchars * random.random()), do_encrypt)] for each_char in range(len(message))])


def main():
    message = input("Input a message: ")
    key = input("Input a key: ")
    while True:
        do_encrypt = input("Encrypt or decrypt the message? (1,0): ")
        if do_encrypt in ('1', '0'):
            break
        print("Please input a valid number,\n"
              "either 0 for decryption or 1 for encryption.")
    print(encrypt(message, key, do_encrypt == '1'))
    input("Press enter to exit.")

if __name__ == '__main__':
    main()