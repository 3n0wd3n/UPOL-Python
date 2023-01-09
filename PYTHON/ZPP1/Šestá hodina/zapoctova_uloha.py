"""
čas na odevzdání: 20.11.2020 9:45
15 bodů
Napište program, který převáde řetězec na binární kod. Předpokládejte, že
řetězec obsahuje pouze velká a malá písmena anglické abecedy, mezery a interpunkci. Například ’Ahoj svete.’. Binární kod řetězce s je řetězec obsahující
za sebe poskládané binární kody znaků řetězce s. Binární kod znaku je řetězec
delky osm obsahujıcı binarnı zapis čısla znaku daneho ASCII. Naprıklad binarnı
kod znaku ’a’ je řetězec ’01100001’. Binární kod retězce ’slunce’ je
011100110110110001110101011011100110001101100101

"""
#První pokus

# slunce = '011100110110110001110101011011100110001101100101'

# string = 'slunce'

# combine_binary = ""
# for i in range(len(string)):
#     char = string[i]
#     char_ord = ord(char)
#     binary = ''
#     remainder = 1
#     while remainder > 0:
#         tem = char_ord % 2
#         remainder = char_ord // 2 
#         if tem == 1:
#             binary = '1' + binary
#         if tem == 0:
#             binary = '0' + binary
#         char_ord = remainder
#     while len(binary) < 8:
#         binary = '0' + binary
#     combine_binary += binary
# print(combine_binary)

# if slunce == combine_binary:
#     print('V pořádku.')
# else:
#     print('Nesoulasí!')



string = 'a'

combine_binary = ""
for i in range(len(string)):
    char = string[i]
    char_ord = ord(char)
    binary = ''
    remainder = 1
    while remainder > 0:
        tem = char_ord % 2
        remainder = char_ord // 2 
        charackter = chr(tem + 48)
        binary = charackter + binary
        char_ord = remainder
    for j in range(8 - len(binary)):
        binary = '0' + binary
    combine_binary += binary
print(combine_binary)

