# Soubor čísel je soubor, který má na každém řádku jedno celé číslo.
#
# Napište funkci, která pro soubor čísel vytvoří soubor jejich druhých
#  mocnin.
#
# Není možné načíst celý soubor do paměti provést výpočet a výsledek
#  uložit do souboru. Je nutné zpracovávat soubor řádek po řádku.
#
# Vaši funkci využijte v programu, který se nejprve zeptá uživatele na
#  zdrojový a poté na cílový soubor. Program dále zavolá vaši funkci,
#  úspěch oznámí uživateli a ukončí se. V případě neúspěchu
#  program uživatele co nejlépe informuje o vzniklé chybě a ukončí se.
#
# Program si musí poradit i se situací, kdy je vstupní soubor ve špatném formátu.
#
# Program nesmí skončit chybou - výpisem chyby interpretu.
#
# Bonusový požadavek: Napište vaší funkci pomocí funkce file_map (obdoby funkce file_filter).

# Odevzdání první verze do 20. dubna 8:45.
# Možnost uznání úkolu do 4. května 8:45.
# Jako předmět e-mailu uveďte ZPP2_1_2. 

# Uložit do zadaného souboru pouze sudá čísla nacházející se v jiném zadaném souboru.
# Není možné celý soubor načíst do paměti.

################################FUNKČNÍ PRVNÍ ČÁST KODU###############################

# def file_numbers_filter(source, target):
#     """Zapíše do souboru target pouze čísla, která splňují predikát."""
#     input_file = open(source)
#     try:
#         output_file = open(target, 'w')
#         try:
#             line = input_file.readline()
#             while line != '':
#                 number = int(line)
#                 if number > 0:
#                     number = number ** 2
#                     output_file.write(str(number) + "\n")
#                 line = input_file.readline() 
#         finally:
#             output_file.close()
#     finally:
#         input_file.close()

# file_numbers_filter('numbers.txt', 'power_numbers.txt')
# while True:
#   counter = 0
#   counter_two = 0
#   def power_numbers(source, target):
#       global counter
#       global counter_two
#       """Zapíše do souboru target pouze čísla, která splňují predikát."""
#       try:
#         input_file = open(source)
#       except FileNotFoundError:
#         counter += 1
#         print("Složka, kterou sjte zadal neexistuje.")
#       except:
#         counter += 1
#         raise RuntimeError('Nelze načíst obsah souboru ' + source)
#       try:
#           try:
#             output_file = open(target, 'w')
#             try:
#               line = input_file.readline()
#             except TypeError:
#               raise RuntimeError('Chyba typu')
#               counter += 1
#             except ValueError:            
#               raise RuntimeError('Chyba hodnoty')
#               counter += 1
#             except FileNotFoundError:
#               raise RuntimeError("Složka, kterou sjte zadal neexistuje.")
#               counter += 1
#             except:
#               raise RuntimeError("Chybí přípona, nebo něco jiného.")
#               counter += 1
#             try:
#               while line != '':
#                   try:
#                     line = line.splitlines()
#                     boole = line[0].isdigit()
#                     if not boole:
#                       counter += 1
#                       return print("Soubor neobsahuje pouze číslice.")
#                     number = line[0]
#                     number = int(number)
#                   except ValueError:
#                     counter += 1
#                     raise RuntimeError('Chyba hodnoty')
#                   except ValueError:
#                     counter += 1
#                     raise TypeError('Chyba typu')
#                   except:
#                     raise RuntimeError("Chyba.")
#                   try:
#                     if number > 0:
#                         number = number ** 2
#                         output_file.write(str(number) + "\n")
#                         counter_two += 1
#                   except:
#                     counter += 1
#                     raise RuntimeError('Odkaz na hodnotu, která ještě nebyla přiřazena')
#                   line = input_file.readline() 
#             except:
#               print("Chyba v zapsání před uložením proměnné")
#           finally:
#               output_file.close()
#       finally:
#         if counter == 0:
#           print("---> Program skončil úspěšně.")
#           input_file.close()
#         if (counter != 0) or (counter_two == 0):
#           print("---> Program skončil neúspěšně!")

#   # V případě, že budete chtít vyzkoušet funkcční verzi zavolejte Soubor s název numbers2.txt a když budete chtít vyzkoušet špatný test, tak zavolejte soubor s názvem txt.txt.
#   print("Bude zadávat zdrojový a cílový soubor.")
#   print('.')
#   print('.')
#   print('.')
#   print('\v')
#   try:
#     source_file = input('Napište porsím zdrojový soubor, ve tvaru název_souboru.txt: ')
#     target_file = input('Napište porsím cílový soubor, ve tvaru název_souboru.txt: ')
#   except NameError:
#     print("Variable x is not defined")
#   except:
#     print("Something else went wrong")
#   power_numbers(source_file, target_file)

while True:
  counter = 0
  counter_two = 0

  def open_source_file(file):
      """Otevře zdrojovou složku"""
      return open(file)

  def open_target_file(file):
      """Otevře cílovou složku"""
      return open(file, 'w')   

  def close_file(file):
      """Zavře složku"""
      file.close()

  def transform_line(line):
      """Převod řádku"""
      global counter
      line = line.splitlines()
      boole = line[0].isdigit()
      if not boole:
        counter += 1
        return False
      transform_number = line[0]
      transform_number = int(transform_number)
      return transform_number

  def powering_number(number, file_to):
        global counter_two
        if number > 0:
            number = number ** 2
            file_to.write(str(number) + "\n")
            counter_two += 1
        return number

  def power_numbers(source, target):
      """Zapíše do souboru target pouze čísla, která splňují predikát."""
      global counter
      global counter_two
      try:
        input_file = open_source_file(source)
      except FileNotFoundError:
        counter += 1
        print("Složka, kterou jste zadal neexistuje")
        raise RuntimeError("Složka, kterou jste zadal neexistuje.")
        # return False
      except:
        counter += 1
        raise RuntimeError('Nelze načíst obsah souboru ' + source)
        # return False
      try:
          try:
            output_file = open_target_file(target)
            try:
              line = input_file.readline()
              print(line)
            except TypeError:
              raise RuntimeError('Chyba typu')
              counter += 1
            except ValueError:            
              raise RuntimeError('Chyba hodnoty')
              counter += 1
            except:
              raise RuntimeError("Chybí přípona, nebo něco jiného.")
              counter += 1
            try:
              while line != '':
                  try:
                    number = transform_line(line)
                    print(number)
                    if number == False:
                          return False
                  except ValueError:
                    counter += 1
                    raise RuntimeError('Chyba hodnoty')
                  except ValueError:
                    counter += 1
                    raise TypeError('Chyba typu')
                  except:
                    raise RuntimeError("Chyba.")
                  try:
                    if number > 0:
                        number = number ** 2
                        output_file.write(str(number) + "\n")
                        counter_two += 1
                  except:
                    counter += 1
                    raise RuntimeError('Chyba v přiřazení hodnoty.')
                  line = input_file.readline() 
            except:
              counter += 1
              print("Chyba v zapsání před uložením proměnné")
              return False
          except:
            counter += 1
            print("Při otevírání složky došlo k chybě.")
            return False
          finally:
              close_file(output_file)
      finally:
        if counter == 0:
          print("---> Program skončil úspěšně.")
          close_file(input_file)
        if (counter != 0) or (counter_two == 0):
          print("---> Program skončil neúspěšně!")

  # V případě, že budete chtít vyzkoušet funkcční verzi zavolejte Soubor s název numbers2.txt a když budete chtít vyzkoušet špatný test, tak zavolejte soubor s názvem txt.txt.
  print("Budete zadávat zdrojový a cílový soubor.")
  print('.')
  print('.')
  print('.')
  print('\v')
  try:
    source_file = input('Zdrojový soubor s příponou .txt: ')
    target_file = input('Cílový soubor s příponou .txt: ')
  except NameError:
    print("Variable x is not defined")
  except:
    print("Something else went wrong")
  power_numbers(source_file, target_file)