def tokenize(TextFilePath) -> list:
    tokenList = []
    #attempts to open a file with the given filepath
    try:
        with open(TextFilePath, 'r') as file:
            for line in file:
                words = line.split()
                #adds the words if they are alphanumeric
                for word in words:
                    #strips non-alphanumeric characters from words
                    result = ''.join(char for char in word if char.isalnum() and char.isascii())
                    if result:
                        tokenList.append(result)

            return tokenList

    except FileNotFoundError:
        print("File not found")

def computeWordFrequencies(tokenList) -> dict:
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

def printFrequencies(wordCount):
    pass

if __name__ == '__main__':
    pass

