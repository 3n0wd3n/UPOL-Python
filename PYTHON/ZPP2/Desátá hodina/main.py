def open_source(source):
  """Otevírá vstupní soubor"""
  try:
      return open(source)
  except PermissionError:
    raise RuntimeError("Nemáte oprávnění k přistupu.")
  except IOError:
    raise RuntimeError("Zaplněný disk, nebo špatný formát souboru.")
  except:
      raise RuntimeError("Nepodařilo se otevřít cílový soubor.")

def open_target(target):
  """Otevírá cílového soubor"""
  try:
      return open(target)
  except PermissionError:
    raise RuntimeError("Nemáte oprávnění k přistupu.")
  except IOError:
    raise RuntimeError("Zaplněný disk, nebo špatný formát souboru.")
  except:
      raise RuntimeError("Nepodařilo se otevřít cílový soubor.")

def transform_line(source_file):
    """Převod řádku"""
    input_file = open_source(source)
    line = input_file.readline()
    counter = 0 
    while line != '':
      line = line.splitlines()
      boole = line[0].isdigit()
      if not boole:
        counter += 1
      line = input_file.readline() 
    return counter != 0

def file_number_map_square(source, target):
    """Čte vstupní soubor a zapisuje do výstupního souboru"""
    source_file = open_source(source)
    try:
        target_file = open(target, 'w')
        try:
            lines = source_file.readlines()
            for line in lines:
              try:
                transform_number = int(line)
                transform_number = transform_number ** 2
                target_file.write(str(transform_number) + "\n")
              except ValueError:
                raise RuntimeError("Soubor neobsahuje pouze čísla.")
        finally:
            target_file.close()
    finally:
        source_file.close()

try:
    counter = 0
    source = input('Zadejte jméno vstupního souboru: ')
    open_source(source)
    target = input('Zadejte jméno výstupního souboru: ')
    open_target(target)
    # are_there_strings = transform_line(source)
    # if not are_there_strings:
    #   file_number_map_square(source, target)
    # elif are_there_strings:
    #   print("Soubor neobsahuje pouze čísla.")
    #   counter += 1
    file_number_map_square(source, target)

except RuntimeError as e:
    print('Chyba:', e)
else:
    if counter == 0:
      print('Program skončil v pořádku.')
    elif counter > 0:
      print('Program skončil neúspěšně.')
    else:
      print('Něco se stalo.')