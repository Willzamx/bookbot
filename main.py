from sys import argv, exit
from stats import get_book_length, get_number_of_this_character, sort_characters

def get_book_text(filePath): 
    return filePath.read()

def build_report(wordsFound,characterDict,bookName):
    report = "============ BOOKBOT ============\n"
    report += f"Analyzing book found at {bookName}...\n"
    report += "----------- Word Count ----------\n"
    report += f"Found {wordsFound} total words\n"
    report += "--------- Character Count -------\n"
    for dict in characterDict:
        if(dict["char"].isalpha()):
            report += f"{dict["char"]}: {dict["num"]}\n"
    report += "============= END ==============="
    print(report)

def main():
    if(len(argv) != 2):
        print("Usage: python3 main.py <path_to_book>")
        exit(1)
    with open(argv[1]) as f:
        text = get_book_text(f)
        build_report(get_book_length(text),sort_characters(get_number_of_this_character(text)),argv[1])
main()