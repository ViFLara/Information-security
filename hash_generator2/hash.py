import  hashlib

string = input("Enter the text to be generated in hash: ")

menu = int(input(''' ### MENU - Choose the type of hash: 
                  1) MD5
                  2) SHA1
                  3) SHA256
                  4) SHA512
                  Enter the number to be generated in hash: '''))

if menu == 1:
    result = hashlib.md5(string.encode('utf-8'))
    print('The MD5 hash of the string: ', string, 'is: ', result.hexdigest())
elif menu == 2:
    result = hashlib.sha1(string.encode('utf-8'))
    print('The SHA1 hash of the string: ', string, 'is: ', result.hexdigest())
elif menu == 3:
    result = hashlib.sha256(string.encode('utf-8'))
    print('The SHA256 hash of the string: ', string, 'is: ', result.hexdigest())
elif menu == 4:
    result = hashlib.sha512(string.encode('utf-8'))
    print('The SHA512 hash of the string: ', string, 'is: ', result.hexdigest())
else:
    print('Something wrong happened, try again')