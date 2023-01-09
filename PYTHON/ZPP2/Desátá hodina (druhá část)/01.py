
def open_source(source):
    """..."""
    try:
        return open(source)
    except:
        raise RuntimeError('Nepodařilo se otevřít zdrojový soubor.')

def file_number_map_square(source, target):
    """..."""
    source_file = open_source(source)
    try:
        target_file = open(target, 'w')        
        try:
            # ...
            # ... int(...)
            # ...
        finally:
            target_file.close()    
    finally:
        source_file.close()

try:
    source = input('...')
    target = input('...')
    file_number_map_square(source, target)
except RuntimeError as e:
    print('Chyba:', e)
else:
    print('Program skončil v pořádku.')