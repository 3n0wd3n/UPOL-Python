file = open('file.txt', 'w')
try:
    file.write('12\n3')
finally:
    file.close()