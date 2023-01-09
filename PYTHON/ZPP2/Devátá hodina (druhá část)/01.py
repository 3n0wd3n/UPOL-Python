file = open('file.txt', 'w')
try:
    file.write('12')
    file.write('\n')
    file.write('3')
finally:
    file.close()