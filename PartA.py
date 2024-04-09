def tokenize(TextFilePath) -> list:
    tokenList = []
    #attempts to open a file with the given filepath
    try:
        with open(TextFilePath, 'r') as file:
            for line in file:
                words = line.split()
                #adds the words if they are unique and alphanumeric
                for word in words:
                    #strips non-alphanumeric characters from words
                    result = ''.join(filter(str.isalnum, word)).lower()
                    if result not in tokenList:
                        tokenList.append(result)
                    else:
                        continue
            return tokenList
    except FileNotFoundError:
        print("File not found")

def computeWordFrequencies(tokenList):
    pass

def printFrequencies(wordCount):
    pass

if __name__ == '__main__':
    pass

