from binary_file import write_byte_list, read_byte_list
file = open('file.bin', 'bw')
write_byte_list(file, [0, 255, 42])
file.close()

# ---

file = open('file.bin', 'br')
read_byte_list(file)
file.close()

# ---


file = open('file.bin')
file.read()
# UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff in position 1: invalid start byte
file.close()

# ---

file = open('file.txt', 'w')
file.write('pláž')
file.close()

# ---

file = open('file.txt', 'br')
read_byte_list(file) # [112, 108, 195, 161, 197, 190]
file.close()

chr(112) # 'p'
chr(108) # 'l'

# ----

file = open('file.bin', 'br+')
read_byte_list(file, 1) # [0]
file.seek(0)
write_byte_list(file, [5])
file.seek(0)
read_byte_list(file) # [0, 255, 42]
file.close()
