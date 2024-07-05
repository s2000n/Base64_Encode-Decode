def base64_encode(input_string):
    base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    binary_string = ''.join([f'{ord(char):08b}' for char in input_string])
    padding_length = (6 - len(binary_string) % 6) % 6
    binary_string += '0' * padding_length
    encoded_string = ''.join([base64_chars[int(binary_string[i:i+6], 2)] for i in range(0, len(binary_string), 6)])
    
    if padding_length == 2:
        encoded_string += '=='
    elif padding_length == 4:
        encoded_string += '='
    
    return encoded_string

def base64_decode(encoded_string):
    base64_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    padding_length = encoded_string.count('=')
    encoded_string = encoded_string.rstrip('=')
    binary_string = ''.join([f'{base64_chars.index(char):06b}' for char in encoded_string])
    
    if padding_length > 0:
        binary_string = binary_string[:-padding_length * 2]
    
    decoded_string = ''.join([chr(int(binary_string[i:i+8], 2)) for i in range(0, len(binary_string), 8)])
    
    return decoded_string

def main():
    print('')
    print('01 - Encode by base64.')
    print('02 - Decode by base64.')
    print('00 - Exit.')
    chose = input('\nEnter your choice: ')
    
    if(chose == '1' or chose == '01'):
        input_string = input("\nEnter your text: ")
        encoded_string = base64_encode(input_string)
        print(f'\nEncoded by base64 is: {encoded_string}')
    elif(chose == '2' or chose == '02'):
        input_string = input("\nEnter your Hash without padding ==: ")
        decoded_string = base64_decode(input_string)
        print(f'\nDcoded by base64 is: {decoded_string}')
    elif (chose == '0' or chose == '00'):
        exit()
    else:
        print('\nWrong choice.')

while True:
    main()