import string

def count_letters_in_file(filename):
    letter_counts = {letter: 0 for letter in string.ascii_lowercase}
    
    try:
        with open(filename, 'r') as file:
            text = file.read().lower() 
            
            for char in text:
                if char in string.ascii_lowercase:
                    letter_counts[char] += 1
        
        sorted_letters = sorted(letter_counts.items(), key=lambda item: (-item[1], item[0]))
        
        output_filename = filename.split('.')[0] + '.hist'
        with open(output_filename, 'w') as output_file:
            for letter, count in sorted_letters:
                if count > 0:
                    output_file.write(f"{letter} -> {count}\n")
        
        print(f"Histogram has been written to {output_filename}")
    
    except FileNotFoundError:
        print("The file was not found.")
        
filename = input("Enter the name of the file: ")
count_letters_in_file(filename)