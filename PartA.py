import sys
def tokenize(TextFilePath: str) -> list:
    tokenList = []
    #attempts to open a file with the given filepath
    try:
        with open(TextFilePath, 'r', encoding = 'utf-8') as file:
            for line in file:
                words = line.split()
                #adds the words if they are alphanumeric
                for word in words:
                    #strips non-alphanumeric characters from words
                    result = ''.join(char for char in word if char.isalnum() and char.isascii())
                    if result:
                        tokenList.append(result.lower())

            return tokenList

    except FileNotFoundError:
        print("File not found")
    except OSError as e:
        print(f"OS error: {e}")

def computeWordFrequencies(tokenList: list) -> dict:
    frequencies = {}
    #runs through all the tokens in the given list
    for token in tokenList:
        #adds 1 to the counter if the entry exists
        if token in frequencies:
            frequencies[token] += 1
        #creates the k/v pair if entry does not exist
        else:
            frequencies[token] = 1

    return frequencies

def printFrequencies(wordCount: dict):
    #sorts the dictionary based on the highest frequency word
    sorted_dict = sorted(wordCount.items(), key = lambda x: (-x[1], x[0]))
    for word, freq in sorted_dict:
        print(f"{word} -> {freq}")


if __name__ == '__main__':
    filePath = sys.argv[1]
    tokens = tokenize(filePath)
    freqCount = computeWordFrequencies(tokens)
    printFrequencies(freqCount)

