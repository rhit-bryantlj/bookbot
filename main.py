def main():
    path = "books/frankenstein.txt"
    book_contents = getContents(path)

    words = book_contents.split()

    contents_lowered = book_contents.lower()
    letterdict = {}
    for letter in contents_lowered:
        if(letter in letterdict):
            letterdict[letter] += 1
        else:
            letterdict[letter] = 1
    sorted_dict = sorted(letterdict.items(), key=lambda item: item[1], reverse = True)
    printReport(path, len(words), sorted_dict)

def printReport(path, words_contained, sorted_dict):
    print(f"--- Begin report of {path} ---")
    print(f"{words_contained} words found in the document\n")

    for pair in sorted_dict:
        if(pair[0].isalpha()):
            print(f"The '{pair[0]}' character was found {pair[1]} times")
    
    print("--- End Report ---")


def getContents(path):
    with open(path) as f:
        return f.read()

if __name__ == '__main__':
    main()