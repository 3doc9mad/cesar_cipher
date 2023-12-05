symbols = '.?!,;:-ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz '

symbols_list = list(symbols)

choice = int(input('1.Encrypt?\n2.Decrypt?\n'))
if choice == 1:
    text_to_encrypt = str(input('Enter text to encrypt: '))
    encrypted_text = ''
    for n in text_to_encrypt:
        if (symbols_list.index(n) + 4) > len(symbols_list):
            encrypted_text += symbols_list[(symbols_list.index(n) + 4 - len(symbols_list))]
        else:
            encrypted_text += symbols_list[(symbols_list.index(n) + 4)]
    print(encrypted_text)
if choice == 2:
    text_to_decrypt = str(input('Enter text to decrypt: '))
    decrypted_text = ''
    for n in text_to_decrypt:
        if (symbols_list.index(n) - 4) < 0:
            decrypted_text += symbols_list[(symbols_list.index(n) - 4 + len(symbols_list))]
        else:
            decrypted_text += symbols_list[(symbols_list.index(n) - 4)]
    print(decrypted_text)
