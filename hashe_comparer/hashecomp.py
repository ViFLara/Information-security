import hashlib

file1 = 'a.txt'
file2 = 'b.txt'

hash1 = hashlib.new('ripemd160')  # 'pemd160' is an algorithm generator

hash1.update(open(file1, 'rb').read())

hash2 = hashlib.new('ripemd160')

hash2.update(open(file2, 'rb').read())

if hash1.digest() != hash2.digest():
    print(f'File: {file1} is different from file: {file2}')
    print(f'The a.txt file hash is: ', hash1.hexdigest())
    print(f'The b.txt file hash is: ', hash2.hexdigest())

else:
    print(f'File: {file1} is the same as file: {file2}')
    print(f'The a.txt file hash is: ', hash1.hexdigest())
    print(f'The b.txt file hash is: ', hash2.hexdigest())
