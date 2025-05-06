import string

def count_letters_in_file(filename):
    letter_counts = {letter: 0 for letter in string.ascii_lowercase} 
    
    try:
        with open(filename, 'r') as file:
            text = file.read().lower()  
            
            for char in text:
                if char in string.ascii_lowercase:
                    letter_counts[char] += 1
        
        for letter in string.ascii_lowercase:
            if letter_counts[letter] > 0:
                print(f"{letter} -> {letter_counts[letter]}")
    
    except FileNotFoundError:
        print("The file was not found.")
        
filename = input("Enter the name of the file: ")
count_letters_in_file(filename)
