def print_file_binary(file_path): 
    with open(file_path, 'rb') as f: 
        while byte := f.read(1): #This returns one byte, not necessarily one UTF-8 characters
            print(format(ord(byte), '08b'), end=' ') #Convert byte to binary

file_path = input('Enter file to display as binary: ')
print_file_binary(file_path) 