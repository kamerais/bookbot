path_to_file = "books/frankenstein.txt"

def main():
    with open(path_to_file) as file:
        text = file.read().lower()
        text_split = text.split()
        number_of_words = len(text_split)
        
        dct = {}
        
        for letter in text:
            if letter.isalpha():
                if letter in dct:
                    dct[letter] += 1
                else:
                    dct[letter] = 1
        
        arrDct = list(dct.items())
        arrDct.sort(key=lambda item: item[1], reverse=True)
        
        
        def print_report():
            print(f"--- Begin report of {path_to_file} ---")
            print(f"{number_of_words} words found in this document")
            print()
            for letter, value in arrDct:
                print(f"The '{letter}' character was found {value} times")
            print("--- End Report ---")
        
        print_report()

main()