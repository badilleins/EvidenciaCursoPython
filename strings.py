for ch in "abc123XYX":
    if ch.isupper():
        print(ch.lower(), end='')
    elif ch.islower():
        print(ch.upper(), end='')
    else:
        print(ch, end='')
 

s1 = 'Where are the snows of yesteryear?'
s2 = s1.split()
print(s2[-2])
 

the_list = ['Where', 'are', 'the', 'snows?']
s = '*'.join(the_list)
print(s)
 
s = 'It is either easy or impossible'
s = s.replace('easy', 'hard').replace('im', '')
print(s)


def mysplit(strng):
    result = []
    word = ''
    
    for char in strng:
        if char.isspace():
            if word:
                result.append(word)
                word = ''
        else:
            word += char
    
    if word:
        result.append(word)
    
    return result

print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))

def display_number(number_str):
    digits = {
        '0': ["###", 
              "# #", 
              "# #", 
              "# #", 
              "###"],
        '1': ["  #", 
              "  #", 
              "  #", 
              "  #", 
              "  #"],
        '2': ["###", 
              "  #", 
              "###", 
              "#  ", 
              "###"],
        '3': ["###", 
              "  #", 
              "###", 
              "  #", 
              "###"],
        '4': ["# #", 
              "# #", 
              "###", 
              "  #", 
              "  #"],
        '5': ["###", 
              "#  ", 
              "###", 
              "  #", 
              "###"],
        '6': ["###", 
              "#  ", 
              "###", 
              "# #", 
              "###"],
        '7': ["###", 
              "  #", 
              "  #", 
              "  #", 
              "  #"],
        '8': ["###", 
              "# #", 
              "###", 
              "# #", 
              "###"],
        '9': ["###", 
              "# #", 
              "###", 
              "  #", 
              "###"]
    }

    lines = [""] * 5
    for digit in number_str:
        if digit in digits:
            for i in range(5):
                lines[i] += digits[digit][i] + " "
        else:
            for i in range(5):
                lines[i] += "??? "

    for line in lines:
        print(line.rstrip())

num = input("Ingrese un numero: ")
if num.isdigit():
    display_number(num)
else:
    print("Solo no negativos.")


def get_valid_shift():
    while True:
        try:
            shift = int(input("Ingrese el desplazamiento (1-25): "))
            if 1 <= shift <= 25:
                return shift
            else:
                print("Ingrese un numero entre 1 y 25.")
        except ValueError:
            print("Ingrese un numero valido.")

def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = chr((ord(char) - base + shift) % 26 + base)
            result += shifted
        else:
            result += char
    return result

text = input("Ingrese texto a encriptar: ")
shift = get_valid_shift()
encrypted = caesar_encrypt(text, shift)
print("Texto encriptado:", encrypted)


def is_palindrome(text):
    if not text.strip():
        return False
    cleaned = ''.join(text.lower().split())
    return cleaned == cleaned[::-1]

text = input("Enter text: ")
if is_palindrome(text):
    print("Es un palíndromo")
else:
    print("No es un palíndromo")


def are_anagrams(text1, text2):
    cleaned1 = ''.join(text1.lower().split())
    cleaned2 = ''.join(text2.lower().split())

    if not cleaned1 or not cleaned2:
        return False

    return sorted(cleaned1) == sorted(cleaned2)

text1 = input("Primer texto: ")
text2 = input("Segundo texto: ")

if are_anagrams(text1, text2):
    print("Anagramas")
else:
    print("No anagramas")

def digit_of_life(birthdate):
    while len(birthdate) > 1:
        total = sum(int(d) for d in birthdate)
        birthdate = str(total)
    return int(birthdate)

date_input = input("Ingresa cumpleaños (Cualquier orden de digitos, 8 digitos total): ")

if not date_input.isdigit() or len(date_input) != 8:
    print("Ingrese 8 digitos exactamente.")
else:
    result = digit_of_life(date_input)
    print(result)


def is_hidden(first, second):
    first = first.lower()
    second = second.lower()
    
    index = 0
    for char in second:
        if index < len(first) and char == first[index]:
            index += 1
        if index == len(first):
            return True
    return False

first = input("Ingrese el primer string: ")
second = input("Ingrese el segundo string: ")

if is_hidden(first, second):
    print("Si")
else:
    print("No")


def is_valid_group(group):
    return sorted(group) == list('123456789')

def read_sudoku():
    sudoku = []
    for _ in range(9):
        row = input()
        if len(row) != 9 or not row.isdigit():
            raise ValueError("Cada fila tiene 9 dígitos.")
        sudoku.append(list(row))
    return sudoku

def check_sudoku(sudoku):
    for row in sudoku:
        if not is_valid_group(row):
            return False
    
    for col in range(9):
        column = [sudoku[row][col] for row in range(9)]
        if not is_valid_group(column):
            return False

    for box_row in range(0, 9, 3):
        for box_col in range(0, 9, 3):
            block = [sudoku[r][c]
                     for r in range(box_row, box_row + 3)
                     for c in range(box_col, box_col + 3)]
            if not is_valid_group(block):
                return False

    return True

try:
    sudoku = read_sudoku()
    print("Si" if check_sudoku(sudoku) else "No")
except ValueError as e:
    print("Datos no validos:", e)

